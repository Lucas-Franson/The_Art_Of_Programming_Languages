# Append text to file
textFile = open('C:/Users/lucas/Documents/Desenvolvimento/The_Art_Of_Programming_Languages/Python/ProgrammingLanguage/example.txt', 'a')

# writing in the file
textFile.write("\nIt's a new line to the file")
textFile.close()

# Read the file
textFile = open('C:/Users/lucas/Documents/Desenvolvimento/The_Art_Of_Programming_Languages/Python/ProgrammingLanguage/example.txt', 'r')

# Read all the file
print(textFile.read())

# Read a part of the file
print(textFile.read(5))

# Read just a line of the file
print(textFile.readline())

# Good practice to close files
textFile.close()

# Writing replace the file
textFile = open('C:/Users/lucas/Documents/Desenvolvimento/The_Art_Of_Programming_Languages/Python/ProgrammingLanguage/example.txt', 'w')

textFile.write("Woops! I have deleted all the text")
textFile.close()

# Creating a new empty file
textFile = open('myfile.txt', 'x')
textFile.close()

# Removing a file
import os
if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('The file does not exist')