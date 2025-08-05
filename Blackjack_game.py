import random

cards = ['A',2,3,4,5,6,7,8,9,10,10,10,10]

dealer = []
player = []

ch = input("Do you want to play the game of Blackjack (Y/N)? ")
if ch in ("Y","y"):
    print("Welcome to the Game!!")
    for i in range(2): 
        dealer.append(random.choice(cards))
        player.append(random.choice(cards))
    
    print(f"Your cards are : {player[0]} and {player[1]}")
    print(f"Dealer's card is : {dealer[0]}")

    choice = input("Do you want to 'hit' or 'stand' : ")
    if choice=="hit":
        player.append(random.choice(cards))
        print(f"Your final cards are : {player[0]}, {player[1]} and {player[2]}")
        while 'A' in player:
            player[player.index('A')] = 11
        if sum(player) > 21 and 11 in player:
            player[player.index(11)] = 1
        if sum(player) > 21 and 11 in player:
            player[player.index(11)] = 1

        print(f"Your sum is equal to {sum(player)}")


        print(f"Dealer's cards are : {dealer[0]} and {dealer[1]}")
        while 'A' in dealer:
            dealer[dealer.index('A')] = 11
        if sum(dealer) > 21 and 11 in dealer:
            dealer[dealer.index(11)] = 1
        
        if sum(dealer) < 17:
            dealer.append(random.choice(cards))
            if dealer[2] == 'A':
                dealer[2] = 11
            if sum(dealer) > 21:
                dealer[2] = 1
            print(f"Dealer's final cards are : {dealer[0]}, {dealer[1]} and {dealer[2]}")
        
        print(f"Dealer's sum is equal to {sum(dealer)}")

        
    elif choice=="stand":
        print(f"Your final cards are : {player[0]} and {player[1]}")
        while 'A' in player:
            player[player.index('A')] = 11
        if sum(player) > 21:
            player[player.index(11)] = 1

        print(f"Your sum is equal to {sum(player)}")


        print(f"Dealer's final cards are : {dealer[0]} and {dealer[1]}")
        while 'A' in dealer:
            dealer[dealer.index('A')] = 11
        if sum(dealer) > 21:
            dealer[dealer.index(11)] = 1

        print(f"Dealer's sum is equal to {sum(dealer)}")

    if sum(player) > 21 and sum(dealer) <= 21:
        print("Sorry, You Lose.")
    elif sum(player) <= 21 and sum(dealer) > 21:
        print("You Win!!")

    else:
        if sum(player) > sum(dealer):
            print("You Win!!")
        elif sum(player) == sum(dealer):
            print("It's a Draw.")
        else:
            print("Sorry, You Lose.")