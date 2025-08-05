import random

def difficulty_level(level):
    if level == "easy":
        print("You get 10 lives! All the best guessing the number :)")
        lives = 10
    elif level == "hard":
        print("You get 5 lives! All the best guessing the number :)")
        lives = 5

    return lives

def check_the_ans(guess,num,lives):
    while lives > 0 and guess != num:
        guess = int(input("Enter your guess : "))
        if guess < num:
            print("\nToo low")
            lives -= 1
            print(f"You have {lives} lives left!")
        elif guess > num:
            print("\nToo High")
            lives -= 1
            print(f"You have {lives} lives left!")
        else:
            print("\nYou Guessed the correct number!!\nYou Won!!")

    if guess != num:
        print("\nYou have now 0 lives left!!\nYou lost :(")

print("Welcome to the number guessing game!!")
print("I am thinking of a number between 1 to 100.")
level = input("Choose your level 'easy' or 'hard' : ")

num = random.randint(1,100)
guess = 0

check_the_ans(guess,num,difficulty_level(level))