import argparse
import os, time
parser = argparse.ArgumentParser()
parser.add_argument("-f","--filename", default=os.path, help="file name", dest="filename")
parser.add_argument("-m", "--mtime", default= os.path.getmtime(os.path), help="time", dest="mtime")
parser.add_argument("-s", "--size", help="size", dest = "size", default=os.path.getsize(os.path))
args = parser.parse_args()
filename = args.filename
mtime = args.mtime
size = args.size
print(filename)
print(mtime)
print(size)
