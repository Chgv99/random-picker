#!/usr/bin/python

import sys
import os
#from PIL import Image
import random
#from datetime import datetime
import time
import datetime
import argparse

parser = argparse.ArgumentParser(description='Pick a random file from directory.')
parser.add_argument('mode', type=str, 
                    help='Choose between multiple or single query modes.')
parser.add_argument('dir', type=str,
                    help='Directory to search.')
parser.add_argument('-b', '--bulk', type=int,
                    default=1,
                    help='Bulk size.')
parser.add_argument('-nl', '--nolog', action='store_true',
                    help='Disables log file for this execution.')
args = parser.parse_args()

#### Directory

path = args.dir
if not os.path.isdir(path):
    raise ValueError("Not a directory.")

####

# class FileType(Enum):
#    IMAGE = 1
#    TEST = 2

# extensions = []

# Extensions
# image = [ ".png", ".jpg", ".png", ".png", ]

# Check for file type
# if keyword == FileType.IMAGE:
#    extensions.append(".png");

#### Files

files = []
for (dirpath, dirnames, filenames) in os.walk(path):
    for x in filenames:
        files.append(os.path.join(dirpath, x))

#### Seed

random.seed(time.time())

#### Open File

def openfile(bulk = 1, log = ""):
    text = ""
    for x in range(bulk):
        file = files.pop(random.randrange(0, len(files)))
        relpath = os.path.relpath(file, args.dir)
        log += "\n\nSelected file:\n\n" + file
        log += "\n\n------------------------------------------"
        text += "\n\nSelected file:\n\n" + os.path.basename(args.dir) + "\\" + relpath
        text += "\n\n------------------------------------------"
        os.startfile(os.path.join(path, file))
    log += "\n"

    if not args.nolog:
        print("esto: " + os.path.dirname(os.path.realpath(__file__)))
        log_path = os.path.dirname(os.path.realpath(__file__)) + "/logs"
        try:
            os.mkdir(log_path, 0o755)
        except:
            pass

        log_file = log_path + "/" + date.strftime("%y-%m-%d") + '.txt'
        file = open(log_file, "a")
        file.write(log)
        print("log at: " + log_file)
        file.close()
    print(text)

#### Mode

if args.mode == "Multiple" or args.mode == "multiple" or args.mode == "M" or args.mode == "m":
    
    #### Date

    date = datetime.datetime.now()
    log = "\n################ " \
          + date.strftime("%H:%M:%S") + " ################\n\n"

    ####
    
    log += "Multiple Mode"
    log += "\n\n------------------------------------------"   
    while True:
        bulk = input("Enter number of files: ")
        if bulk == "":
            print("Exiting multiple mode.")
            break;
        bulk = int(bulk)

        openfile(bulk=bulk, log=log)
elif args.mode == "Single" or args.mode == "single" or args.mode == "S" or args.mode == "s":
    
    #### Date

    date = datetime.datetime.now()
    log = "\n################ " \
          + date.strftime("%H:%M:%S") + " ################\n\n"

    ####

    if args.bulk > 1:
        log += "Bulk: Yes\n\nBulk size: " + str(args.bulk)
    else:
        num = 1
        log += "Bulk: No"
    log += "\n\n------------------------------------------"    

    openfile(bulk=args.bulk, log=log)
#elif args.mode == "":

else:
    print("\"" + str(args.mode) + "\" is not a valid mode. ")