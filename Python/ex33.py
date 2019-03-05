#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 33: While Loops
# Date:     March 5, 2019
#
# a while-loop will keep executing the code block under it as long as a
# Boolean expression is True.
#
# What they do is simply do a test like an if-statement, but instead of
# running the code block once, they jump back to the 'top' where the while-
# loop starts and repeats the logic. A while-loop runs until the expression
# is False.
#
# Rules:
#
# 1. Make sure that you use while-loops sparingly.
#    Usually a for-loop is better.
#
# 2. Review your while statements and make sure that the
#    Boolean test will become False at some point.
#
# 3. When in doubt, print out your test variable at the top and bottom
#    of the while-loop to see what it's doing.
#
i = 0
numbers = []

while i < 6:
    print(f"At the top, i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom, i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# end of script #
