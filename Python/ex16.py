#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 16: Reading and Writing Files
# Date:     February 22, 2019
#

# make a simple little text editor
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# note: no need to use truncate() since target is presumed to be a new file
#       and the use of 'w' by default truncates the file to 0 bytes
#       see here for more information:
#       https://stackoverflow.com/questions/26917197/behaviour-of-truncate-method-in-python
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()

# end of script #
