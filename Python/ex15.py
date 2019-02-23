#
# Author:   Cristain E. Nuno
# Purpose:  Exercise 15: Reading Files
# Date:     Feburary 22, 2019
#

# we do not want to 'hard code' file paths into our script
# 'hard coding' means putting some bit of information that should
# come from the user as a string directly in our source code.
#
# the solution is to use argv or input to ask the user what file to use
#

# imports necessary modules ----
from sys import argv

# unpacks input and stores it as filename
script, filename = argv

# txt returns the file object in filename
txt = open(filename)

# prints the filename back to console
print(f"Here's your file {filename}:")
# reads the file object and prints to console
print(txt.read())

# prints command
print("Type the filename again:")
# user sees '> ' to guide them to entering the filename
file_again = input("> ")

# txt_again returns the file object in filename
txt_again = open(file_again)

# reads the file object and prints to console
print(txt_again.read())

# end of script #
