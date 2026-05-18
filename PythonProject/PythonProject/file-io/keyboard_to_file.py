def KeyboardToFileCopy():
    file = open("../file/keyboard.txt", "w")
    text = input('Enter your message = ')

    while (text != "quit"):
        file.write(text)
        file.write("\n")
        text = input('')
    file.close()

KeyboardToFileCopy()