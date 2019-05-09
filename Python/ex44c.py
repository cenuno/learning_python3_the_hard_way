#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 44C: Alter Before or After
# Date:     April 28, 2019
#
summary = """
The third way to use inheritance is a special case of overriding where you
want to alter the behavior before or after the Parent class's version runs.

You first override the function just like in the last example, but then
you use a Python built-in function named super to get the Parent version to
call.
"""

print(summary)


class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def altered(self):
        # executes as expected
        print("CHILD, before PARENT altered()")
        # use super to get the Parent.altered version
        # i.e. call super with arguments Child and self,
        #      then call the function altered on whatever it returns
        super(Child, self).altered()
        # executes as expected
        print("CHILD, after PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()

# end of script #
