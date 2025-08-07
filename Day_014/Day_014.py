import random as r
import data as d

def choosing_options(data):
    person1 = r.choice(data)
    person2 = r.choice(data)

    while person1 == person2:
        person2 = r.choice(data)

    return person1, person2

def game(p1,p2,score,data):
    print(f"Compare A: {p1['name']}, {p1['description']}, {p1['country']}.")
    print(f"Against B: {p2['name']}, {p2['description']}, {p2['country']}.")
    
    choice = input("Who has more followers on Instagram? Type 'A' or 'B' : ")
    if p1['follower_count'] >= p2['follower_count']:
        ans = "A"
    else:
        ans = "B"
    
    if choice == ans:
        score += 1
        print("\nHigher or Lower")
        print(f"You're right!! Your current score is {score}")
        data.remove(p1)
        p1, p = choosing_options(data)
        game(p2,p1,score,data)
    else:
        print("\nHigher or Lower")
        print(f"Sorry, That's wrong your final score is {score}")



print("Higher or Lower")
score = 0
p1, p2 = choosing_options(d.data)
game(p1,p2,score,d.data)