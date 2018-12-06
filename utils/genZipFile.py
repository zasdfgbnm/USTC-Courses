# coding: utf-8
import os
import shutil
from zipfile import ZipFile
from operator import or_
from functools import reduce
from config import WALKDIR


def checkZip(name):
    '''check if this file should be added to the zip'''
    li = [name.startswith('.') ,name.endswith('.zip'),name.lower()=='readme.md']
    return not any(li)
def genZipFile(tar = WALKDIR,rewrite=False):
    os.chdir(tar)
    n = len(tar)
    gen = os.walk(tar)
    pwd = os.path.abspath('.')
    for path, dirs, files in gen:
        li = path.strip(os.sep).split(os.sep)
        if any([i[0]=='.' for i in li]) or 'index.html' in files :continue
        ziplst = []
        for i in files:
            if i.endswith('个文件.zip'):
                if rewrite:
                    os.remove(os.path.join(path,i))
                else:break
            elif checkZip(i):
                ziplst .append(i)
        else:
            if len(ziplst)<3:continue
            ziplst.sort()
            tmp = os.path.abspath(path) \
                    .replace(pwd,'')\
                    .replace(os.sep,'-')
            name = '{tmp}目录下的{length}个文件.zip'.format(tmp=tmp,length =len(ziplst))
            zipName = os.path.join(path,name)
            try:
                with ZipFile(zipName,'w') as z:
                    os.chdir(path)
                    for i in ziplst: z.write(i)
            except Exception as e:
                print(e)


def checkBigFile():
    big = os.path.join(WALKDIR,'.bigFile')
    if not os.path.exists(big):
        os.mkdir(big)
    gen = os.walk(WALKDIR)
    for path,dirs,files in gen:
        li = path.strip(os.sep).split(os.sep)
        if reduce(or_,[i[0]=='.' for i in li],False):continue
        for file in files:
            filePath = os.path.join(path,file)
            size = os.path.getsize(filePath)
            if size > (2**20)*100:
                print('[BIG]: {} is bigger than 100mb'.format(filePath))
                try:
                    shutil.move(filePath,big)
                except Exception as e:
                    print(e)
                    os.remove(filePath)



if __name__ == '__main__':
    #genZipFile(rewrite=True)
    genZipFile(rewrite=False)
    checkBigFile()
