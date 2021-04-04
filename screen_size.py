#
# script to calculate screen width & height, given it's diagonal and height:width ratio
#
import math
import argparse

# for inches -to- cm conversions
CM_PER_INCH = 2.54
MM_PER_CM = 10


def screenSize(diag, relativeWidth, relativeHeight):
    # given a screen-size (as a diagonal-size) and the aspect-ratio of the wridth-to-height
    #  use Pythagoras-theorem to calculate the actual-width & -height of that screen
    #
    # inputs are:
    #  diag, rw, rh
    #
    # and we need to calculate
    #  w, h
    #
    # and so the math is:
    #     w / h = rw / rh
    #  => w     = (rw / rh) * h                  **
    #  Pythagoras: w^2 + h^2 = diag^2
    #  => ((rw / rh) * h)^2 + h^2 = diag^2   replacing w from ** above
    #  => (1 + (rw/rh)^2) * h^2 = diag^2     factorising the h^2
    #  => h^2 = diag^2 / (1 + (rw/rh)^2)     re-arrange for h^2
    #  => h = diag / sqrt(1 + (rw/rh)^2)     take positive sqrt to solve for h
    #
    # so now we have calculated h
    #  then substitute this into ** line to solve for w.
    #
    height = diag / math.sqrt(1 + pow(relativeWidth / relativeHeight, 2))
    width = (relativeWidth / relativeHeight) * height
    return [width, height]


def dpi(widthInches, horizontalPixels):
    return horizontalPixels / widthInches


def inToCm(inches):
    return inches * CM_PER_INCH


def dpiToDpCm(dpi):
    return dpi / CM_PER_INCH


def dotPitch(diagInches, ppi):
    diagPixels = ppi * diagInches
    return diagInches * CM_PER_INCH * MM_PER_CM / diagPixels


def printUserScreenSize():
    parser = argparse.ArgumentParser(
        description='Calculate actual screen-width and -height - from given diagonal screen-size & aspect ratio, e.g. --diag 32 --rw 16 --rh 9 (representing a 32", 16:9 screen). Optionally include DPI output - if pixel-width is provided (e.g. --pixels 3840 for a 4K screen)')
    parser.add_argument('--dp', dest='decimal_places', type=int,
                        help='# of decimal places for the output (int, default 2)', nargs=1, default=[2])
    parser.add_argument('--pixels', dest='horizontal_pixels',
                        type=int, help='# of pixels across 1-row of screen', nargs=1)
    required = parser.add_argument_group('Required args')
    required.add_argument('--diag', dest='diagonal_size', type=float,
                          help='actual diagonal size of screen (inches, float)', nargs=1, required=True)
    required.add_argument('--rw', dest='relative_width', type=int,
                          help='relative width of screen (int)', nargs=1, required=True)
    required.add_argument('--rh', dest='relative_height', type=int,
                          help='relative height of screen (int)', nargs=1, required=True)
    args = parser.parse_args()
    diag = args.diagonal_size[0]
    rw = args.relative_width[0]
    rh = args.relative_height[0]
    dp = args.decimal_places[0]
    dimensions = screenSize(diag=diag, relativeWidth=rw, relativeHeight=rh)
    width = dimensions[0]
    height = dimensions[1]
    calculateDpi = args.horizontal_pixels is not None
    if calculateDpi:
        pixels = args.horizontal_pixels[0]
        ppi = dpi(width, pixels)
        ppiS = ppi * ppi
        dotPitchMm = dotPitch(diagInches=diag, ppi=ppi)
    print("inches (Imperial)")
    print(
        f" {diag}\"-screen has 'width x height' of '{width:.{dp}f}\" x {height:.{dp}f}\"'")
    if calculateDpi:
        print(f'  DPI = {ppi:.{dp}f}')
        print(f'  DPI^2 = {ppiS:.{dp}f}')
    print("cm (Metric)")
    print(f" {inToCm(diag):.{dp}f}cm-screen has 'width x height' of '{inToCm(width):.{dp}f}cm x {inToCm(height):.{dp}f}cm'")
    if calculateDpi:
        ppCm = dpiToDpCm(ppi)
        ppSCm = ppCm * ppCm
        print(f'  Pixels-per-CM = {ppCm:.{dp}f}')
        print(f'  Pixels-per-Square-CM = {ppSCm:.{dp}f}')
        print(f'  Dot-Pitch = {dotPitchMm:.{dp}f}mm')


if __name__ == '__main__':
    printUserScreenSize()
