from basic.INPUT_FUNTION import choice

students= []

# add stdent
def add_student():
    name = input("ENTER STUDENT NAME")
    roll = input("NETER YOUR ROLL NUMBER")

    student = {
        "name" : name,
        "roll" : roll
    }

    students.append(student)
    print("student added  successfull")

# ================= SHOW STUDENTS FUNCTION =================

# Saare students show karne ka function
def show_students():
    if len(students) == 0:

        print("NO STUDENTT NAME")


    else:
    # Heading print
      print("\n STYDENT LIST>\n")

    for i in students:

        print("name > >", i["name"])

        print("roll > >", i["roll"])

        print("__________________________")

# ================= SEARCH STUDENT FUNCTION =================
def search_student():

    roll = input("ENTER YOUR ROLL NUMBER")
    found = False

    for i in students:
       if i["roll"] == roll:

           print("STUDENT FONUD")

           print("name", i["name"])

           print("roll", i["roll"])
    found = True

    if found == False:
        print("STUDENT NAME")


def del_student():

    roll = input("ENTER  ROLL NUMBER TO DELETE:")

    for i in students:
        if i["roll"] == roll:

            students.remove(i)

            print("STUDENT DELETED SUCCESFULL")

            return

        print("STUDENT NOT FOUND")


# ================= MAIN PROGRAM =================
while True:

    print("\n STUDENT MANGMENT FUNTION ")

    print("1. add student")
    print("2. show student")
    print("3. search student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("enter your choice:")

    if choice ==  "1":
        add_student()

    elif  choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        del_student()

    elif choice == "5":
        print("program close")
        break

    else:
        print("INVALID CHOICE")









