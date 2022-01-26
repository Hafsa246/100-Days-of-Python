import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's name seperated by a comma. \n")
names = nameAsCSV.split(", ")

# print(names)
pay = random.choice(names)
print(f"{pay} is going to buy the meal today!")

# length = len(names)
# random_choice = random.randint(0, length-1)
# person = names[random_choice]
# print(f"{person} is going to buy the meal today!")