class Student:


    def __init__(self, name, marks, colleg_name):
        self.name = name
        self.marks = marks
        self.colleg_name = colleg_name


    def detail(self):
        print("student name   >", self.name)
        print("student marks >",self.marks)
        print("student colleg_name >", self.colleg_name)
        print("______________________")

s1 = Student("farhan ali khan", 97, "'vikrant group of instutation ")
s2 = Student("abdulla", 67, "'vikrant group of instutation ")
s3 = Student("rohit thakur", 40, "'vikrant group of instutation ")

s1.detail()
s2.detail()
s3.detail()
