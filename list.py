import os,sys
#path = sys.argv[1]


def listdir(path):
    print("HI")
    fileList = os.listdir(path)
    for file in fileList:
        if os.path.isdir(path+"\\"+file):
            listdir(path+"\\"+file)

            print("DIR >> "+ path +"\\"+file )
        else:
            print("FILE >> "+ path+"\\"+ file)

#listdir(path)