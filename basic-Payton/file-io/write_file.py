def writefile():
    file = open("../files/write.txt", "w")
    file.write("hi/n")
    file.write("hello farhan khan /n")
    file.write("i am b.tech student")
    print("file write succssfull>>>>")
    file.close()




writefile()