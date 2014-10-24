#Extensible Dictionary System v1.0 - Reads .txt Files

print("Welcome to Simple Dictionary v1.0\n")
print("Enter the name of the file to read:")
read = input()

with open(read) as out_file:
  word = out_file.read()
print(word)
