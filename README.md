# Screen Size

Small python3 script to calculate screen-width & -height from a given diagonal-size and aspect ratio. Screen DPI can also be calculated - see usage below

Remember that in real life, you'll need to add extra width & height for the bezel, and likely some height for the stand. But at least this allows you to appreciate the space taken up by the screen alone. Could be helpful in designing that ultimate work-from-home office!

## How to use

```
$ python screen_size.py -h
usage: screen_size.py [-h] [--dp DECIMAL_PLACES] [--pixels HORIZONTAL_PIXELS] --diag DIAGONAL_SIZE --rw RELATIVE_WIDTH --rh RELATIVE_HEIGHT

Calculate actual screen-width and -height - from given diagonal screen-size & aspect ratio, e.g. --diag 32 --rw 16 --rh 9 (representing a 32",
16:9 screen). Optionally include DPI output - if pixel-width is provided (e.g. --pixels 3840 for a 4K screen)

optional arguments:
  -h, --help            show this help message and exit
  --dp DECIMAL_PLACES   # of decimal places for the output (int, default 2)
  --pixels HORIZONTAL_PIXELS
                        # of pixels across 1-row of screen

Required args:
  --diag DIAGONAL_SIZE  actual diagonal size of screen (float)
  --rw RELATIVE_WIDTH   relative width of screen (int)
  --rh RELATIVE_HEIGHT  relative height of screen (int)
```

## Example

Screen size calculations:

```
$ python screen_size.py --diag 43 --rw 16 --rh 9
43.0"-screen has 'width x height' of '37.48 x 21.08'
```

Include DPI, e.g. for a 4K screen the horizontal pixels is 3840:

```
$ python screen_size.py --diag 43 --rw 16 --rh 9 --pixels 3840
43.0"-screen has 'width x height' of '37.48 x 21.08'
DPI = 102.46
```

Richard Shepherd.

April, 2021