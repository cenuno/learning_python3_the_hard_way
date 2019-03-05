#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 29: What If
# Date:     March 4, 2019
#
# introduction to the if-statement
people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

# note: remember += is an increment operator that
#       adds/subtracts value to a variable
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

# end of script #
