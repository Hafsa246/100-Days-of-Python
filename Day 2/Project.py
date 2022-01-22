bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? "))
people = float(input("How many people are splitting the bill? "))
res = (bill + (bill*(tip/100)))/people
print(f"Each person should pay: {res}")