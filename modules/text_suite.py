def write_text():
    print("File name:")
    name = input()
    print("Text:")
    fileContents = input()
    #Creating the file
    with open(name, "wt") as out_file:
        out_file.write(fileContents)


def read_text():
    print("Enter the name of the file to read:")
    read = input()

    with open(read) as out_file:
        word = out_file.read()
    print(word)


def error():
    print("SHOOT! An error. Something went wrong. Sorry!")


def xyzzy():
    print("That doesn't work in this program. Play ADVENTURE if you want to do that!")
