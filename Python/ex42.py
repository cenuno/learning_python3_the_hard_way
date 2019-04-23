#
# Author:       Cristian E. Nuno
# Date:         April 22, 2019
# Purpose:      Is-A, Has-A, Objects, and Classes
#
# You can use the phrase 'is-a' when you talk about objects and classes
# being related to each other by a class relationship.
#
# You use 'has-a' when you talk about objects and classes that are related
# only because they reference each other.
#

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Make a class named Dog that is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a __init__ that takes self and name params
        self.name = name

## Make a class named Cat that is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes self and name params
        self.name = name

## Make a class named Person that is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name params
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Make a class named Employee that is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## super can be used to refer to parent classes without
        ## naming them explicitly, thus making the code more maintainable.
        ## https://docs.python.org/3/library/functions.html#super
        super(Employee, self).__init__(name)
        ## class Employee has-a __init__ that takes salary params
        self.salary = salary

## Make a class named Fish that is-a object
class Fish(object):
    pass

## Make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

## Make a class named Halibut that is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## from mary get the pet attribute and set it to satan
mary.pet = satan

## frank is-a Employee who makes $120 salary
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

# end of script #
