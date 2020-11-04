from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together

INPUT_PATH = r'.\input'
OUTPUT_PATH = r'.\output'

to_convert = [join(INPUT_PATH, f) for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]

print(to_convert)

for image in to_convert:
    Image.open(image)
