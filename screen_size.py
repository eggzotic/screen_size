#
# script to calculate screen width & height, given it's diagonal and height:width ratio
#
import math
import argparse


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
    #  w / h = rw / rh
    #  => w = (rw / rh) * h                  **
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


def printUserScreenSize():
    parser = argparse.ArgumentParser(
        description='Calculate actual screen-width and -height - from given diagonal screen-size & aspect ratio, e.g. --diag 32 --rw 16 --rh 9 (representing a 32", 16:9 screen). Optionally include DPI output - if pixel-width is provided (e.g. --pixels 3840 for a 4K screen)')
    parser.add_argument('--dp', dest='decimal_places', type=int,
                        help='# of decimal places for the output (int, default 2)', nargs=1, default=[2])
    parser.add_argument('--pixels', dest='horizontal_pixels',
                        type=int, help='# of pixels across 1-row of screen', nargs=1)
    required = parser.add_argument_group('Required args')
    required.add_argument('--diag', dest='diagonal_size', type=float,
                          help='actual diagonal size of screen (float)', nargs=1, required=True)
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
    print(
        f"{diag}\"-screen has 'width x height' of '{width:.{dp}f} x {height:.{dp}f}'")
    if args.horizontal_pixels is not None:
        pixels = args.horizontal_pixels[0]
        ppi = dpi(width, pixels)
        print(f'DPI = {ppi:.{dp}f}')


if __name__ == '__main__':
    printUserScreenSize()
