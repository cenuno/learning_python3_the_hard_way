#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 6: Strings and Text
# Date:     February 19, 2019
#

# programmers love saving time at your expense by using annoyingly short and
# cryptic variable names, so let's get you started reading and writing them
# early on

# integer variable
types_of_people = 10

# format string
x = f"There are {types_of_people} types of people."

# string variable s
binary = "binary"
do_not = "don't"
# format string
y = f"Those who know {binary} and those who {do_not}."

# print statements
print(x)
print(y)

# print statements w/format strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# boolean variable
hilarious = False
# format string
joke_evaluation = "Isn't that joke so funny?! {}"

# print statement w/format syntax
print(joke_evaluation.format(hilarious))

# string variables
w = "This is the left side of..."
e = "a string with a right side."

# concatenating two string variables inside one print statement
print(w + e)

# end of script #
