import pickle



class Employee:
    def __init__(self, id, name, salary ):
        self.id = id
        self.name = name
        self.id = id
        self.salary = salary


    def display(self):
        print(self.id, "\t", self.name, "\t", self.salary)


with open("../file/person.txt", 'wb') as file:
    per = Employee(1, "farhaan ali khan ", 10000)
    pickle.dump(per, file)