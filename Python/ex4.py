#
# Author:       Cristian E. Nuno
# Purpose:      Exercise 4: Variables and Names
# Date:         February 19, 2019
#

# a variable is nothing more than a name for something
cars = 100
space_in_cars = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about"
        , average_passengers_per_car
        , "in each car.")

# end of script #
