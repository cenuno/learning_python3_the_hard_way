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

# prints prompt
print("Type the filename:")
# user sees '> ' to guide them to entering the filename
filename = input("> ")

# txt returns the file object in filename
txt = open(filename)

# reads the file object and prints to console
print(txt.read())

# close the file and immediately free up any system resources used by it
txt.close()

# end of script #
