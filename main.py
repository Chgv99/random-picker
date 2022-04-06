import sys
import os
#from PIL import Image
import random
#from datetime import datetime
import time
import datetime
import argparse

parser = argparse.ArgumentParser(description='Pick a random file from directory.')
parser.add_argument('dir', type=str,
                    help='Directory to search.')
parser.add_argument('--bulk', type=int,
                    default=1,
                    help='Bulk size.')
parser.add_argument('--log',
                    help='Saves log.')
args = parser.parse_args()

# class FileType(Enum):
#    IMAGE = 1
#    TEST = 2

# Params
# keyword = sys.argv[1]

date = datetime.datetime.now()
log = "\n############ " \
      + date.strftime("%d-%m-%y %H:%M:%S") + " ############\n\n"

#path = sys.argv[1]
path = args.dir
if (len(sys.argv) > 2):
    num = int(sys.argv[2])
    log += "Bulk: Yes\n\nBulk size: " + str(num)
else:
    num = 1
    log += "Bulk: No"
log += "\n\n-------------------------------------------"

# extensions = []

# Extensions
# image = [ ".png", ".jpg", ".png", ".png", ]

if not os.path.isdir(path):
    raise ValueError("Not a directory.")

# Check for file type
# if keyword == FileType.IMAGE:
#    extensions.append(".png");

files = []
for (dirpath, dirnames, filenames) in os.walk(path):
    for x in filenames:
        # if x.endswith(".shp"):
        # print(os.path.join(dirpath, x))
        files.append(os.path.join(dirpath, x))

random.seed(time.time())
for x in range(num):
    file = files.pop(random.randrange(0, len(files)))

    log += "\n\nSelected file:\n\n" + file
    log += "\n\n-------------------------------------------"

    os.startfile(os.path.join(path, file))
log += "\n"
print(log)
