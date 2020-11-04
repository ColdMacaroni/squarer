from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together

INPUT_PATH = r'.\input'
OUTPUT_PATH = r'.\output'

to_convert = [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]

print(to_convert)

transparent = [True if input('Y for transparent, N for blur: ').strip().lower() in ['y', 'yes'] else False]

for image in to_convert:
    old_img = Image.open(join(INPUT_PATH, image))

    x, y = old_img.size  # Get size in pixels

    big_side, small_side = max([x, y]), min([x,y]) # Get biggest and smallest side for creating the square

    new_image = Image.new('RGBA', (big_side, big_side), (0, 0, 0, 0)) # Square canvas. Size lenght of biggest_side

    # To get where to paste the image:
    #   Coords are from top left to bottom right
    #   Biggest side's coords are 0 so it stays in line with the new canvas
    #   new side's coords are (biggest_side-small_side)/2, gets the difference and splits it so the image is at the middle

    new_image.paste(old_img)

    # Get rid of extension
    # Allows for filenames to have . in them
    filename = image.split('.')
    del filename[-1]
    '.'.join(filename)

    # Save with the new extension
    new_image.save(filename + '.png')
