#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 44B: Override Explictly
# Date:     April 28, 2019
#
summary = """
The problem with having functions called implicitly is sometimes
you want the child to behave differently. In this case you want to
override the function in the child, effectively replacing the
functionality. To do this, just define a function
with the same name in Child.
"""

print(summary)


class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

dad.override()
son.override()

reflection = """
Parent.override() executes because that variable (dad)
is a Parent. But when line 15 runs, it prints out the Child.override
messages because son is an instance of Child and Child overrides that function
by defining its own version.
"""

print(reflection)

# end of script #
