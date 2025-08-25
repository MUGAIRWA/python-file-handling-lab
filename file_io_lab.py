# program that reads a file and writes a modified version to a new file.
file = open("input.pdf", "r")
content = file.read()

# Modify the content i.e convert to uppercase
modified_content = content.upper()

# Write the modified content to a new file
new_file = open("output.pdf", "w")
new_file.write(modified_content)
new_file.close()

print("Modified content written to 'output.pdf'")

# File Read & Write with Error Handling 
# user inputs file name
filename = input("Enter filename to read: ")

# error handling
try:
    file = open(filename, "r")   # try to open the file
    content = file.read()

    print(" File read successfully")
except FileNotFoundError:
    print("Error: The file you entered does not exist.")