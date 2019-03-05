#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 27: Memorizing Logic
# Date:     March 4, 2019
#

# learning logic has to come after you do memorization
print('''
and: as in one condition AND two condition must be satisifed to be TRUE
i.e. 3 and 5 are both greater than 2 is {}.
'''.format(3 > 2 and 5 > 2))

print('''
or: as in one condition OR two condition must be satisifed to be TRUE
i.e. 3 or 5 is less than 4 is {}.
'''.format(3 < 4 or 5 < 4))

print('''
not: as in a condition is NOT satisfied to be TRUE
i.e. not False is {} because False is not True.
'''.format(not False))

print('''
not is commonly to paired with in to test for non-membership within a group
i.e. 3 not in [0, 1, 2, 4, 5] is {}.
'''.format(3 not in [0, 1, 2, 4, 5]))

# end of script #
