class Person:
    count = 0
    def __init__(self):
        self.name = ''
        self.address = ''
        Person.count += 1

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

p = Person()
p.set_name('abc')
p.set_address('123 Indore')
print('Name:', p.get_name())
print('Address:', p.get_address())
# print('Count:', Person.count)
# print('Memory address of p:', id(p)

p1 = Person()
p1.set_name('xyz')
print('Name:', p1.get_name())
# print('Count:', Person.count)
# print('Memory add
# ress of p1:', id(p1))