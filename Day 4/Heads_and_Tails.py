import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)  #assigns a number to a specific ouput 
# for e.g if u type 431 it will generate randomly head or tail and then remember it for this certain number
number = random.randint(0,1)
if number == 1:
    print("Heads")
else:
    print("Tails")
