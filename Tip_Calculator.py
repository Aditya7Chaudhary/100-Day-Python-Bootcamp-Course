print("Welcome to the tip calculator!")
bill = int(input("What was the total bill ? : "))
tip = int(input("How much tip will you like to give ? : "))
people = int(input("How many people are splitting the bill ? : "))

total_bill = bill*(1+tip/100)
net_bill = round(total_bill/people, 3)

print(f"Each person should pay : ${net_bill}")
