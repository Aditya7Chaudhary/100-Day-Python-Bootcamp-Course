import random as r

word_list = ["Apple","Orange","Mango","Banana","Jackfruit","Pinapple","Kiwi","Strawberry","Dragonfruit"]
word = r.choice(word_list)

guess = "_"*len(word)
Guess_word = list(guess)
lives = 5

print("Welcome to the Hangman Game!")
print(f"You have to guess this word : {guess}")
print("All the best!!")

while "".join(Guess_word) != word and lives>0:
    letter = input("Enter a letter : ")
    Guess_word = list(Guess_word)
    index = 0
    f = 0
    for i in word:
        if letter==i:
            Guess_word[index] = letter
            f = 1
        index = index + 1
    
    guess = "".join(Guess_word)

    if f==0:
        lives = lives-1
        print("Oops! Wrong guess you lose 1 heart")
        print(f"Now you have {lives} left!")
        print(f"Word = {guess}")
        print("")
    else:
        print("Great guess!")
        print(f"Now you have {lives} left!")
        print(f"Word = {guess}")
        print("")

if lives == 0:
    print("Game Over!!\nYou Lost the game.")
    print(f"The word to guess was : {word}")

elif guess == word:
    print("Congratulations!!\nYou guessed the correct word!")
    print(f"The answer was indeed : {word}")