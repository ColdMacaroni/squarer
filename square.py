from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together

BLUR_INPUT_PATH = r'.\blur_input'
TRANSPARENT_INPUT_PATH = r'.\transparent_input'
OUTPUT_PATH = r'.\output'

to_convert = [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]

print(to_convert)


for image in to_convert:
    old_img = Image.open(join(INPUT_PATH, image))

    x, y = old_img.size  # Get size in pixels

    big_side, small_side = max([x, y]), min([x,y]) # Get biggest and smallest side for creating the square

    new_image = Image.new('RGBA', (big_side, big_side), (0, 0, 0, 0)) # Square canvas. Size lenght of biggest_side

    # To get where to paste the image:
    #   Coords are from top left to bottom right
    #   Biggest side's coords are 0 so it stays in line with the new canvas
    #   new side's coords are (big_side-small_side)/2, gets the difference and splits it so the image is at the middle

    # Calculation here inpendent of the stuff.
    special_coord = int((big_side-small_side)/2)

    # If the x side is the biggest
    if big_side == x:
        new_image.paste(old_img, (0, special_coord))

    elif big_side == y:
        new_image.paste(old_img, (special_coord, 0))

    else:
        print('Something has gone really wrong')
        continue

    # Get rid of extension
    # Allows for filenames to have . in them
    filename = image.split('.')
    del filename[-1]
    new_filename = '.'.join(filename)

    # Save with the new extension
    new_image.save(join(OUTPUT_PATH, new_filename + '.png'))

    # Close those boys up
    new_image.close()
    old_img.close()
