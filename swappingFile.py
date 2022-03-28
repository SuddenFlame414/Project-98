def swapFileData():
    fileName =  input("Enter the file name:- ")

    file =  open(fileName)
    x=file.read()
    print(x)


swapFileData()