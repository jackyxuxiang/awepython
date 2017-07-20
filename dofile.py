import os

filepath="."

listfile = os.listdir(filepath)
for fname in listfile:
    stateinfo = os.stat(filepath+"/"+fname)
    print(stateinfo.st_atime)
    print(fname)

#haha
