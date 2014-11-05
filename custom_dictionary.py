#Please fill in this sequence with the names of your text files
uniqueID = [0, 2, "etc.txt"]

print("Welcome to Simple Dictionary v1.0\n")
print("Enter the index value of the file:")
read = input()
read_file = int(read)

with open(uniqueID[read_file]) as out_file:
    word = out_file.read()
print(word)