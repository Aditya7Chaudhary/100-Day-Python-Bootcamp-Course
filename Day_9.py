import os

def clear_terminal():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Mac and Linux (posix)
        _ = os.system('clear')

bids = {}

choice = "y"

while choice in ("Y","y"):
    print("Welcome to the Bidding contest!!")
    name = input("Enter your name : ")
    bid = int(input("Enter your bid : "))
    
    bids[name] = bid
    choice = input("Is anyone left to put their Bid? (Y/N) : ")

    clear_terminal() 

max = 0
for key in bids:
    if bids[key] > max:
        i = key
        max = bids[key]

print(f"The maximum bid is given by {i} = {bids[i]}")