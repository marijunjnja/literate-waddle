#!/usr/local/bin/env python3.7
import os, re, sys, json

importedfile = sys.argv[1]
with open(importedfile, 'r') as f:
    fileinfo = json.load(f)

source = fileinfo['source']
destination = fileinfo['destination']
filetypes = fileinfo['filetypes']

imgarray = []
totalimages = 0

masterlist = "_master_list.txt"
fileregex = f"{destination}/([0-9]+){masterlist}"

for root, dirs, files in os.walk(destination):
    for name in files:
        fullname = f"{root}/{name}"
        filesearch = re.search(fileregex, fullname, re.IGNORECASE) 
        if filesearch:
            totalimages = int(filesearch.group(1))

for root, dirs, files in os.walk(source):
    for name in files:
        if name.endswith(tuple(filetypes)):
            totalimages += 1
            imgarray.append(f"{root}/{name} ==> {totalimages}_{name}\n")
            os.rename(f"{root}/{name}", 
                        f"{destination}/{totalimages}_{name}")

with open(f"{destination}/{totalimages}{masterlist}", 'w') as f:
    for file in imgarray:
        f.write("%s\n" % file)

