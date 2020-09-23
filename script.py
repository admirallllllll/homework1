import argparse
import os, time
file = os.stat("dz1.py")
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mtime", help="time", action = "store_true")
parser.add_argument("-s", "--size", help="size", action = "store_true")
parser.add_argument("--rename", help="rename", action="store_true")
args = parser.parse_args()
mtime = args.mtime
size = args.size
rename = args.rename
if mtime:
    print("last modified: %s" % time.ctime(st.st_mtime))
if size:
    print("size: %s" %file.st_size)
if rename:
    os.rename('dz1.py', 'B.py')
