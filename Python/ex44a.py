#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 44A: Implicit Inheritance
# Date:     April 28, 2019
#
summary = """
Inheritance is used to indicate that one class will get most or all
of its features from a parent class. This happens implicitly whenever
you write class Foo(Bar), which says
"Make a class Foo that inherits from Bar".

When you do this, the language makes any action that you do on instances
of Foo also work as if they were done to an instance of Bar. Doing this
lets you put common functionality in the Bar class, then specialize
that functionality in the Foo class as needed.

3 ways the parent and child classes interact:
- Actions on the child impliy an action on the parent;
- Actions on the child override the action on the parent;
- Actions on the child alter the action on the parent.


~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implicit Inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implicty actions that happen when you define a function in the parent
but not in the child
"""
print(summary)


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    """
    Creates a class named Child but says there's nothing new to define it
    """
    # create an empty block
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

reflection = """
Notice how even though I'm calling son.implict() & even though Child()
does not have an implict function defined, it still works, and it calls
the one defined in Parent.

This shows you that if you put functions in a base class (i.e. Parent)
then all subclasses (i.e. Child) will automatically get those features.

Very handy for repetive code you need in many classes.
"""

print(reflection)

# end of script #
