import os

def find_big_files(path,size):
    '''找大文件'''
    files = os.listdir(path)
    for f in files:
        p1 = path+f
        #是不是文件
        isfile = os.path.isfile(p1)
        #size
        size = os.path.getsize(p1)
        if isfile:
            print(p1+" is file " + str(size))
        else:
            print(p1 + " is dir ")

find_big_files("/Users/junjun/Documents/",10)