import pickle
from  write_object_file import Employee


with open("../file/person.txt", 'rb' ) as file:
    obj = pickle.load(file)
    print("Printing Employee information after unpickling")


obj.display()