class india:
    def country (self):
        print("india is a country")


    def language(self):
        print("india has many languages")

    def culture(self):
        print("india has a rich culture")

class usa:
    def country (self):
        print("usa is a country")


    def language(self):
        print("usa has many languages")

    def culture(self):
        print("usa has a rich culture")


ind = india()
usa = usa()
for con in (ind,usa):
    con.country()
    con.language()
    con.culture()