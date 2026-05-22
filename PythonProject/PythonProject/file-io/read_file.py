def readfile():
    file = open("C:/Users/ACER/Desktop/read_file.txt",'r' )

    text = file.read()
    print(text)
    file.close()

readfile()