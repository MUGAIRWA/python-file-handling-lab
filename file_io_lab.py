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

