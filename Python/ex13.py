#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 13: Parameters, Unpacking, Variables
# Date:     February 21, 2019
#

# import necessary modules ----
from sys import argv
# whatever is in argv, unpack it and assign it
# to all of these variables on the left in order
script, first, second = argv
third = input("What is your thid variable? ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# end of script #
