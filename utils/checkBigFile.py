def checkBigFile():
    big = os.path.join(WALKDIR,'.bigFile')
    if not os.path.exists(big):
        os.mkdir(big)
    gen = os.walk(WALKDIR)
    for path,dirs,files in gen:
        li = path.strip(os.sep).split(os.sep)
        if any([i[0]=='.' for i in li]):continue
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
if __name__=='__main__':
    checkBigFile()
