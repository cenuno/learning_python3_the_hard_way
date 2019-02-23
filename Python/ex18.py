#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 18: Names, Variables, Code, Functions
# Date:     February 23, 2019
#
# Functions do three things:
# 1. They name pieces of code the way variables name strings and numbers
# 2. They take arguments the way your scripts take argv
# 3. Using 1 and 2, they let you make your own 'mini-scripts' or 'tiny commands'
#

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# end of script #
