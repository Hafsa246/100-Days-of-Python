print("Welcome to the Rollercoaster")
height = int(input("What is your height? "))
bill = 0
age = int(input("What is your age? "))
if (height >= 120):
    if(age >= 18):
        bill = 12
        # print("kindly pay 12 dollars")
    elif(age <18 and age > 12):
        bill = 7
        # print("kindly pay 7 dollars")
    else:
        bill = 5
        # print("Kindly pay 5 dollars")
    photo = input("Do you wanta photo? Y or N? ")
    if(photo == 'Y'):
        bill += 3
    print(f"Kindly pay {bill} dollars")
    
else:
    print("You are not allowed")