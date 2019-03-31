#
# Author:   Cristian E. Nuno
# Purpose:  Exercise 39: Dictionaries, Oh Lovely Dictionaries
# Date:     March 30, 2019
#

# note: mapping (or associating) is the key concept in a dictionary
dashes = "-" * 10

# create a mapping of state to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": ("Detroit", "Ann Arbor"),
    "FL": "Jacksonville"
}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print(dashes)
print("NY State has:", cities["NY"])
print("OR State has:", cities["OR"])

# print some states
print(dashes)
print("Michigan's abbreviation is:", states["Michigan"])
print("Florida's abbreviation is:", states["Florida"])

# do it by using the state then cities dict
print(dashes)
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Florida"]])

# print every state abbreviation
print(dashes)

# convert the dictionary to a list of tuples, storing the results in state & abbrev
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviatied {abbrev}.")

# print every city in state
print(dashes)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")

# now do both at the same time
print(dashes)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviatied {abbrev} and has city {cities[abbrev]}.")
print(dashes)

# safely get a abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get("TX", "Does Not Exist!")
print("The city for the state 'TX' is:", city)

# end of script #
