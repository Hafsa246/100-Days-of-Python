print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined = name1+name2
newname = combined.lower()
t = newname.count("t")
r = newname.count("r")
u = newname.count("u")
e = newname.count("e")

true = t+r+u+e

l = newname.count("l")
o = newname.count("o")
v = newname.count("v")
e = newname.count("e")

love = l+o+v+e

ans = int(str(true) + str(love))

if(ans<10 or ans>90):
    print(f"Your score is {ans}, you go together like coke and mentos")
elif(ans>40 and ans<50):
    print(f"Your score is {ans}, you are alright together")
else:
    print(f"Your score is {ans}")