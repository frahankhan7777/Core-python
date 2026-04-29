class student:
    def getstudent(self):
        self.name = input("name")
        self.age = input("age")
        self.gender = input("gender")


class test(student):

    def getmarks(self):
        self.studentclass = input("class:")
        print("enter the marks of the respective subject")
        self.literature = int(input("literature"))
        self.math = int(input("math" ))
        self.biology = int(input("biology"))
        self.physics = int(input("physics"))


class marks(test):
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("gender:",self.gender )
        print("class:", self.studentclass)
        print("literature:", self.literature)
        print("math:", self.math)
        print("biology:", self.biology)
        print("physics:", self.physics)
        total_marks = self.literature + self.math + self.biology + self.physics
        if total_marks > 100:
            print("pass")
        else:
            print("fail")
        print("total marks:", total_marks)

m = marks()
m.getstudent()
m.getmarks()
m.display()