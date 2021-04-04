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


def printUserScreenSize():
    parser = argparse.ArgumentParser(
        description='Calculate actual screen-width and -height - from given actual diagonal screen-size, relative screen-width & -height, e.g. --diag 32 --rw 16 --rh 9 (representing a 32", 16:9 screen)')
    parser.add_argument('--dp', dest='decimal_places', type=int,
                        help='# of decimal places for the output (default 2)', nargs=1, default=[2])
    required = parser.add_argument_group('Required args')
    required.add_argument('--diag', dest='diagonal_size', type=int,
                          help='actual diagonal size of screen', nargs=1, required=True)
    required.add_argument('--rw', dest='relative_width', type=int,
                          help='relative width of screen', nargs=1, required=True)
    required.add_argument('--rh', dest='relative_height', type=int,
                          help='relative height of screen', nargs=1, required=True)
    args = parser.parse_args()
    diag = args.diagonal_size[0]
    rw = args.relative_width[0]
    rh = args.relative_height[0]
    dp = args.decimal_places[0]
    dimensions = screenSize(diag=diag, relativeWidth=rw, relativeHeight=rh)
    print(
        f"Screen size with diagonal of {diag} has 'width x height' of '{dimensions[0]:.{dp}f} x {dimensions[1]:.{dp}f}'")


if __name__ == '__main__':
    printUserScreenSize()
