#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 17: More Files
# Date:     February 22, 2019
#

# we'll write a Python script to copy one file to another
# it'll be very short but will give you ideas about other things
# you can do with files

# load necessary modules ----
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# open and read the from_file object
in_file = open(from_file).read()

print(f"The input file is {len(in_file)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(in_file)

print("Alright, all done.")

out_file.close()

# end of script #
