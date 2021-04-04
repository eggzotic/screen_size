# Screen Size

Small python3 script to calculate screen-width & -height from a given diagonal-size and aspect ratio. Remember that in real life, you'll need to add extra width & height for the bezel, and likely some height for the stand. But that at least allows you to appreciate the space taken up by the screen alone.

## How to use

```
$ python screen_size.py -h
usage: screen_size.py [-h] [--dp DECIMAL_PLACES] --diag DIAGONAL_SIZE --rw RELATIVE_WIDTH --rh RELATIVE_HEIGHT

Calculate actual screen-width and -height - from given actual diagonal screen-size, relative screen-width & -height, e.g. --diag
32 --rw 16 --rh 9 (representing a 32", 16:9 screen)

optional arguments:
  -h, --help            show this help message and exit
  --dp DECIMAL_PLACES   # of decimal places for the output (default 2)

Required args:
  --diag DIAGONAL_SIZE  actual diagonal size of screen (float)
  --rw RELATIVE_WIDTH   relative width of screen (int)
  --rh RELATIVE_HEIGHT  relative height of screen (int)
```

## Example

```
$ python screen_size.py --diag 43 --rw 16 --rh 9
Screen size with diagonal of 43 has 'width x height' of '37.48 x 21.08'
```

Richard Shepherd.

April, 2021