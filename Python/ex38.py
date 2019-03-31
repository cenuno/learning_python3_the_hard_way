#
# Author:   Cristian E. Nuno
# Purpose:  Doing Things to Lists
# Date:     March 30, 2019
#

# note: lists have many methods (i.e. functions) that allows us to do stuff
#       by using the my_list.foo syntax, where . (period) operator
#       accesses all of the list methods
my_list = ["hello", "goodbye"]
print("{} is the original list".format(my_list))
my_list.append("or are we dancer?")

# note: my_list is not being reassigned. the append automatically saves elements
print("{} is after we append a new element inside the original list".format(my_list))

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

for i in (10 - len(stuff)):
    # note: more_stuff will constantly decrease with each call of .pop()
    print(more_stuff)
    # take the last element of more_stuff and store it in next_one
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # note: no need to reassign the value of stuff as .append() does it for us
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    i += 1

print("There we go: ", stuff)

print("Let's do some things with stuff.")

# give me the element at index 1
print(stuff[1])

# give me the last element
print(stuff[-1]) # whoa! fancy

# give me the last element but also remove it from stuff
print(stuff.pop())
print(stuff)

# flatten the list into a character string separated by one space " "
print(" ".join(stuff)) # what? cool!

# flatten the 3 and 4 index into a character string by one pound sign "#"
print("#".join(stuff[3:5])) # super stellar!

# end of script #
