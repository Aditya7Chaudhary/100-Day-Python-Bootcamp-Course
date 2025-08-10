from random import shuffle

class Quiz():
    def asking_the_question(self,question):
        score = 0
        count = 0
        shuffle(question)
        for q in question[0:10]:
            print(q.text, end = " : ")
            ans = input()
            if ans == q.ans:
                score += 1
                count += 1
                print("You have got it right!!")
                print(f"The correct answer was : {q.ans}")
                print(f"Your score is {score}/{count}\n")
            else:
                count += 1
                print("You have got it wrong!!")
                print(f"The correct answer was : {q.ans}")
                print(f"Your score is {score}/{count}\n")
        print(f"Game Over, Your final score is {score}/{count}")