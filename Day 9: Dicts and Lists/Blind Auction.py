from turtle import clear
from art import logo
print(logo)

bids = {}

def highest_bid(bids):
    highest = 0
    winner = ""
    for i in bids:
        bid_amnt = bids[i]
        if bid_amnt>highest:
            highest = bid_amnt
            winner = i
    print(f"The winner is {winner} with a bid of ${highest}")

ask = True
while(ask):
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    bids[name] = price

    ask = input("Any other users who want to bid? Type 'yes' or 'no' ")
    if ask == "no":
        ask = False
        highest_bid(bids)
    elif ask == "yes":
        clear()