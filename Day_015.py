def coffee_machine(resources):
    drink = input("\nWhat would you like? ")

    if drink == "latte":
        ing = drink_ingridients(drink)
    elif drink == "cappuccino":
        ing = drink_ingridients(drink)
    elif drink == "espresso":
        ing = drink_ingridients(drink)
    elif drink == "report":
        print("These are the resources:")
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        money = resources["money"]
        print(f"Water = {water} ml")
        print(f"Milk = {milk} ml")
        print(f"Coffee = {coffee} g")
        print(f"Money = $ {money}")
        coffee_machine(resources)
    elif drink == "off":
        exit()
    else:
        print("We don't have that Coffee.")
        coffee_machine(resources)
    
    if check_ingredients(ing,resources):
        coins = {}
        coins["penny"] = int(input("How many Penny : "))
        coins["nickel"] = int(input("How many Nickel : "))
        coins["dime"] = int(input("How many Dime : "))
        coins["quarter"] = int(input("How many Quarter : "))

        if check_money(drink,coins,resources):
            for i in ing:
                resources[i] -= ing[i]
        print(f"Here is your {drink}")
        coffee_machine(resources)
    else:
        coffee_machine(resources)
        

def drink_ingridients(drink):
    if drink == "latte":
        ingredients = {"water":200, "coffee":24, "milk":150}
    elif drink == "cappuccino":
        ingredients = {"water":250, "coffee":24, "milk":100}
    elif drink == "espresso":
        ingredients = {"water":50, "coffee":18, "milk":0}

    return ingredients

def check_money(drink,coins,resources):
    value = coins["penny"] + coins["nickel"]*5 + coins["dime"]*10 + coins["quarter"]*25
    value /= 100

    if drink == "espresso":
        if value == 1.5:
            resources["money"] += 1.5
            return True
        elif value < 1.5:
            print("Sorry the amount is not enough")
            print(f"Money refunded back : {value}")
            coffee_machine(resources)
            return False
        else:
            resources["money"] += 1.5
            print(f"Your change is {value-1.5}")
            return True

    elif drink == "latte":
        if value == 2.5:
            resources["money"] += 2.5
            return True
        elif value < 2.5:
            print("Sorry the amount is not enough")
            print(f"Money refunded back : {value}")
            coffee_machine(resources)
            return False
        else:
            resources["money"] += 2.5
            print(f"Your change is {value-2.5}")
            return True

    elif drink == "cappuccino":
        if value == 3.0:
            resources["money"] += 3.0
            return True
        elif value < 3.0:
            print("Sorry the amount is not enough")
            print(f"Money refunded back : {value}")
            coffee_machine(resources)
            return False
        else:
            resources["money"] += 3.0
            print(f"Your change is {value-3.0}")
            return True

def check_ingredients(ing,resources):
    l = []
    if ing["water"] > resources["water"]:
        l.append("water")
    if ing["coffee"] > resources["coffee"]:
        l.append("coffee")
    if ing["milk"] > resources["milk"]:
        l.append("milk")

    if len(l) == 3:
        print(f"Sorry there is not enough {l[0]}, {l[1]} and {l[2]}")
        return False
    elif len(l) == 2:
        print(f"Sorry there is not enough {l[0]} and {l[1]}")
        return False
    elif len(l) == 1:
        print(f"Sorry there is not enough {l[0]}")
        return False
    else:
        return True

def machine_resources():
    resources = {}
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    resources["money"] = 0

    return resources


print("Welcome to the Coffee Machine Project!!")
print("Kindly place your order :)")
coffee_machine(machine_resources())