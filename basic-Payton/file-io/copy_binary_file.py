import shutil


source = "C:/Users/ACER/Downloads/demo.JPEG"
target = "C:/Users/ACER/Desktop/python photo/faran.jpg"


shutil.copyfile(source, target)
print(source , " is copy into " , target)