from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type this file name again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())