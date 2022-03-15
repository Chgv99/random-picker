import sys
import os
#from PIL import Image
import random
#from datetime import datetime
import time

#class FileType(Enum):
#    IMAGE = 1
#    TEST = 2

# Params
#keyword = sys.argv[1]
path = sys.argv[1]
print(path)
extensions = []

# Extensions
#image = [ ".png", ".jpg", ".png", ".png", ]

if not os.path.isdir(path):
    raise ValueError("Not a directory.")

# Check for file type
#if keyword == FileType.IMAGE:
#    extensions.append(".png");

files = []
for (dirpath, dirnames, filenames) in os.walk(path):
    files.extend(filenames)

random.seed(time.time())
file = files.pop(random.randrange(0, len(files)))
print("Selected file: " + file)

#im = Image.open(os.path.join(path, f))
#im.show()
os.startfile(os.path.normpath(os.path.join(path, file)))
