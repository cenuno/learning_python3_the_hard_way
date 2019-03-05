#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 28: Boolean Practice
# Date:     March 4, 2018
#

# boolean logic is used everwhere in programming. it is fundamental part of
# computation, and knowing the expressiongs is akin to knowing your scales
# in music.

print("True and True is {}.".format(True and True)) # True
print("False and True is {}.".format(False and True)) # False
print("1 == 1 and 2 == 1 is {}".format(1 == 1 and 2 == 1)) # False
print("'test' == 'test' is {}.".format("test" == "test")) # True
print("1 == 1 or 2 != 1 is {}.".format(1 == 1 or 2 != 1)) # True
print("True and 1 == 1 is {}.".format(True and 1 == 1)) # True
print("False and 0 != 0 is {}.".format(False and 0 != 0)) # False
print("True or 1 == 1 is {}".format(True or 1 == 1)) # True
print("'test' == 'testing' is {}.".format("test" == "testing")) # False
print("1 != 0 and 2 == 1 is {}.".format(1 != 0 and 2 == 1)) # False
print("'test' != 'testing' is {}.".format("test" != "testing")) # True
print("'test' == 1 is {}.".format("test" == 1)) # False
print("not (True and False) is {}.".format(not (True and False))) # True
print("not (1 == 1 and 0 != 1) is {}.".format(not (1 == 1 and 0 != 1))) # False
print("not (10 == 1 or 1000 == 1000) is {}."
        .format(not (10 == 1 or 1000 == 1000))) # False
print("not ('testing' == 'testing' and 'Zed' == 'Cool Guy') is {}."
        .format(not ("testing" == "testing" and "Zed" == "Cool Guy"))) # True
print("1 == 1 and (not ('testing == 1 or 1 == 0')) is {}."
        .format(1 == 1 and (not ("testing" == 1 or 1 == 0)))) # True
print("'chunky' == 'bacon' and (not (3 == 4 or 3 == 3)) is {}."
        .format("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))) # False
print("3 == 3 and (not ('testing' == 'testing' or 'Python' == 'Fun')) is {}."
        .format(3 == 3 and
                (not ("testing" == "testing" or "Python" == "Fun")))) # False

# end of script #
