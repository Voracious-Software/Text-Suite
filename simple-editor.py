print("WELCOME TO SIMPLE TEXT EDITOR! PLEASE NAME YOUR FILE:")
name = input()
print("NOW WRITE YOUR TEXT:")
fileContents = input()
#Creating the file
with open(name, "wt") as out_file:
    out_file.write(fileContents)
