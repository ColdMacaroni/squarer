from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together

to_convert = [f for f in listdir(r'.\input') if isfile(join(r'.\input', f))]

print(to_convert)
