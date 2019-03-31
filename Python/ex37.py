#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 37: Symbol Review
# Date:     March 30, 2019
#

# getting more comfortable with lists
my_list = ["luke", "kylo", "han", "R2D2", "obi-wan", "rey", "luke", "leia"]

print("my_list is a list of star wars characters:\n{}.".format(my_list))

print("{} is first index where 'luke' appears".format(my_list.index("luke")))

print("{} is all instances of 'luke' within my_list".format([i for i in my_list if i == "luke"]))

# end of script #
