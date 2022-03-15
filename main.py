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
if (len(sys.argv) > 2):
    num = int(sys.argv[2])
else:
    num = 1

#extensions = []

# Extensions
#image = [ ".png", ".jpg", ".png", ".png", ]

if not os.path.isdir(path):
    raise ValueError("Not a directory.")

# Check for file type
#if keyword == FileType.IMAGE:
#    extensions.append(".png");

files = []
for (dirpath, dirnames, filenames) in os.walk(path):
    for x in filenames:
        #if x.endswith(".shp"):
        #print(os.path.join(dirpath, x))
        files.append(os.path.join(dirpath, x))
print("files: ")
print(files)

random.seed(time.time())
for x in range(num):
    file = files.pop(random.randrange(0, len(files)))
    print("Selected file: " + file)

    # im = Image.open(os.path.join(path, f))
    # im.show()
    print("path: ")
    print(os.path.normpath(os.path.join(path, file)))
    print(os.path.join(path, file))

    os.startfile(os.path.join(path, file))
