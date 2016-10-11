import os
from fnmatch import fnmatch

root = '/Users/liamkleyn/Desktop/scrapescript/puku2/www.puku.co.za/Books'
pattern = "*.html"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print os.path.join(path, name)