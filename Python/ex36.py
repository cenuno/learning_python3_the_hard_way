#
# Author:       Cristian E. Nuno
# Purpose:      Exercise 36: Designing and Debugging
#               (code a little, run a little, fix a little)
# Date:         March 28, 2019
#
# Rules for if-statements -----
# 1. every if-statement must have an else
# 2. if this else should never run because it doesn't make sense,
#    then you must use a die function in the else that prints out an
#    error message and dies. This will find many errors
# 3. Never nest if-statements more than two deep and always try to do them
#    more than one deep
# 4. Treat if-statements like paragraphs, where each if-elif-else grouping
#    is like a set of sentences. Put blank lines before and after
# 5. Your Boolean tests should be simple. If they are complex, move their
#    calculations to variables earlier in your function and use a good name for
#    the variable
#
# Rules for Loops ----
# 1. Use a while-loop only to loop forever, and that means probably never.
#    This only applies to Python; other languages are different.
# 2. Use a for-loop for all other kinds of looping, especially if there is a
#    fixed or limited number of things to loop over.
#
from sys import exit
import datetime

def the_present():
    year = datetime.datetime.today().strftime("%Y")
    year = int(year)
    return(year)

def dead(why):
    print(why, "Game over!")
    exit(0)

def start():
    print("What is your birth year?")

    birth_year = int(input("> "))

    if birth_year < 1900:
        message = "Your birth year of {} occured before 1900.\nPlausible but highly unlikely."

        dead(message.format(birth_year))

    elif birth_year > the_present():
        message = "Your birth year of {} occurs after {}.\nAre you related to Marty McFly?."

        dead(message.format(birth_year, the_present()))
    else:
        print("Your birth year seems legit. Carry on.")

start()
# end of script #
