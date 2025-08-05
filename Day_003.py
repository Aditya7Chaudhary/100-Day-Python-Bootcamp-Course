print("Welcome to the Python Pizza Deliveries!")
size = input("What Size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want the pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want the extra cheese? Y or N: ")

if size in ("S","s"):
    price = 15
elif size in ("M","m"):
    price = 20
elif size in ("L","l"):
    price = 25
else:
    print("Error")

if pepperoni in ("Y","y"):
    price += 3
if extra_cheese in ("Y","y"):
    price += 1

print(f"Your total bill is ${price}")
