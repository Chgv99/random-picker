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
parser.add_argument('-b', '--bulk', type=int,
                    default=1,
                    help='Bulk size.')
parser.add_argument('-nl', '--nolog', action='store_true',
                    help='Disables log file for this execution.')
args = parser.parse_args()

# class FileType(Enum):
#    IMAGE = 1
#    TEST = 2

# Params
# keyword = sys.argv[1]

date = datetime.datetime.now()
log = "\n################ " \
      + date.strftime("%H:%M:%S") + " ################\n\n"

#path = sys.argv[1]
path = args.dir
#print(args.bulk)
#if (len(sys.argv) > 2):
if args.bulk > 1:
    log += "Bulk: Yes\n\nBulk size: " + str(args.bulk)
else:
    num = 1
    log += "Bulk: No"
log += "\n\n------------------------------------------"

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
text = ""
for x in range(args.bulk):
    file = files.pop(random.randrange(0, len(files)))
    relpath = os.path.relpath(file, args.dir)
    log += "\n\nSelected file:\n\n" + file
    log += "\n\n------------------------------------------"
    text += "\n\nSelected file:\n\n" + os.path.basename(args.dir) + "\\" + relpath
    text += "\n\n------------------------------------------"


    os.startfile(os.path.join(path, file))
log += "\n"

if not args.nolog:
    #log_det + log
    try:
        os.mkdir('logs', 0o755)
    except:
        pass

    log_file = r'logs/' + date.strftime("%y-%m-%d") + '.txt'
    file = open(log_file, "a")
    file.write(log)
    file.close()
print(text)
