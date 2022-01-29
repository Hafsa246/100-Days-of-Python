# Function 
# def greet():
#     print("Hello")
#     print("I hope you are doing well")
#     print("Enjoy your day, Keep learning")
# greet()

## Function with parameters 
# def greet_name(name):
#     print(f"Hello {name}")
#     print(f"I hope you are doing well {name}")
#     print("Enjoy your day, Keep learning")
# greet_name("Hafsa")


## name (parameter) = hafsa (argument) 

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"I hope you like our city {location} :)")


name = input(("What's your name? "))
location = input(("What's your loation? "))

greet_with(name, location)