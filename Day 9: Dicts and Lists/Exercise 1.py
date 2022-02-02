# {Key: Value}
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Bug"])
programming_dictionary["Loop"] = "Maybe Something"
# print(programming_dictionary)

# Create an empty dictionary 
empty_dictionary = {}

# Clearing a dictionary 
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary 
programming_dictionary["Bug"] = "Trying to change this"
# print(programming_dictionary)

#prints out only keys
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
