#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 34: Accessing Elements of Lists
# Date:     March 5, 2019
#

# Python starts its lists at 0 rather than 1. It seems weird,
# but there are many advantages to this, even though it is mostly arbitrary.
#
# ordinal == ordered, 1st;
#
# cardinal == cards at random, 0.
#
animals = ['bears', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

print(f'''
Here are all my animals:
{animals}
''')
print("The animal at 1 is {}.".format(animals[1]))
print("The third animal is {}.".format(animals[2]))
print("The first animal is {}.".format(animals[0]))
print("The animal at 3 is {}.".format(animals[3]))
print("The fifth animal is {}.".format(animals[4]))
print("The animal at 2 is {}".format(animals[2]))
print("The sixth animal is {}.".format(animals[5]))
print("The animal at 4 is {}.".format(animals[4]))

# end of script #
