import argparse
import os, time
st = os.stat("dz1.py")
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mtime", help="time", action = "store_true")
parser.add_argument("-s", "--size", help="size", action = "store_true")
parser.add_argument("--rename", help="rename")
args = parser.parse_args()
mtime = args.mtime
size = args.size
rename = args.rename
if mtime:
    print("last modified: %s" % time.ctime(st.st_mtime))
if size:
    size1 = st.st_size
    size2 = size1 / 1024
    print("size: %s" % size2)
if rename:
    os.rename('dz1.py', str(rename))
