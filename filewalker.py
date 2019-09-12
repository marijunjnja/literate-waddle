#!/usr/local/bin/env python3.7
import os, re, sys, json

importedfile = sys.argv[1]
with open(importedfile, 'r') as f:
    fileinfo = json.load(f)

source = fileinfo['source']
destination = fileinfo['destination']
filetypes = fileinfo['filetypes']

filelist = []
totalfiles = 0

masterlist = "_master_list.txt"
fileregex = f"{destination}/([0-9]+){masterlist}"

for root, dirs, files in os.walk(destination):
    for name in files:
        fullname = f"{root}/{name}"
        filesearch = re.search(fileregex, fullname, re.IGNORECASE) 
        if filesearch:
            totalfiles = int(filesearch.group(1))

for root, dirs, files in os.walk(source):
    for name in files:
        if name.endswith(tuple(filetypes)):
            totalfiles += 1
            filelist.append(f"{root}/{name} ==> {totalfiles}_{name}\n")
            os.rename(f"{root}/{name}", 
                        f"{destination}/{totalfiles}_{name}")

with open(f"{destination}/{totalfiles}{masterlist}", 'w') as f:
    for file in filelist:
        f.write("%s\n" % file)

