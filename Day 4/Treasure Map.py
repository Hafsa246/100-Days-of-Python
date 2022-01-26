from turtle import pos, position


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

emoji = ("x")

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Your choices are 11,12,13,21,22,23,31,32,33:\n")

print("The first coordinate is: " + position[0])
print("The second coordinate is: " + position[1])

if position[0] == "1":
    if position[1] == "1":
        row1[0] = emoji
    elif position[1] == "2":
        row1[1] = emoji
    elif position[1] == "3":
        row1[2] = emoji
    else:
        print("That's impossible")

elif position[0] == "2":
    if position[1] == "1":
        row2[0] = emoji
    elif position[1] == "2":
        row2[1] = emoji
    elif position[1] == "3":
        row2[2] = emoji
    else:
        print("That's impossible")

elif position[0] == "3":
    if position[1] == "1":
        row3[0] = emoji
    elif position[1] == "2":
        row3[1] = emoji
    elif position[1] == "3":
        row3[2] = emoji
    else:
        print("That's impossible")

else:
    print("That's not a choice.")


print(f"{row1}\n{row2}\n{row3}")