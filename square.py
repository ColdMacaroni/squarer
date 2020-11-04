from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together

INPUT_PATH = r'.\input'
OUTPUT_PATH = r'.\output'

to_convert = [join(INPUT_PATH, f) for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]

print(to_convert)

transparent = [True if input('Y for transparent, N for blur: ').strip().lower() in ['y', 'yes'] else False]

for image in to_convert:
    old_img = Image.open(image)

    x, y = old_img.size

    big_side, small_side = max([x, y]), min([x,y])

    new_image = Image.new('RGBA', (big_side, big_side), (0, 0, 0, 0))

    # To get where to paste the image:
    #   Coords are from top left to bottom right
    #   Biggest side's coords are 0 so it stays in line with the new canvas
    #   new side's coords are (biggest_side-small_side)/2, gets the difference and splits it so the image is at the middle
