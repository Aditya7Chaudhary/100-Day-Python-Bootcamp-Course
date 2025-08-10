from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    ques = Question(q['text'],q['answer'])
    question_bank.append(ques)

quiz = Quiz()
quiz.asking_the_question(question_bank)
        