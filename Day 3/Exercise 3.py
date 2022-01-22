height = float(input("What is your height? "))
weight = float(input("What is your weight? "))
bmi = round(weight/height**2)

if(bmi < 18.5):
    print(f"Your bmi is {bmi} and You are Underweight")
elif(bmi < 25):
    print(f"Your bmi is {bmi} and You have a normal weight")
elif(bmi < 30):
    print(f"Your bmi is {bmi} and You are Overweight")
elif(bmi < 35):
    print(f"Your bmi is {bmi} and You are Obese")
else:
    print(f"Your bmi is {bmi} and You are clinically obese")