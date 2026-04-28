import datetime
class Person:
    AVG_AGE = 18

    def __init__(self):
        self.name  = None
        self.dob = None
        self.address = None

    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name

    def set_dob(self,dob):
        self.dob = dob
    def get_dob(self):
        return self.dob

    def set_address(self,address):
        self.address = address
    def get_address(self):
        return self.address

    def get_age(self):
        if self.dob is None:
            return None
        now = datetime.datetime.now()
        old = now.year - self.dob.year
        return old

per = Person()
per.set_name("Keshav")
per.set_dob(datetime.datetime(2007,5,20))
per.set_address("Maheshwar")

print("Your name is :",per.get_name())
print("Your date of birth is :",per.get_dob())
print("Your address is :",per.get_address())
print("You are",per.get_age(),"year old")
print("Person's average age is :",Person.AVG_AGE)