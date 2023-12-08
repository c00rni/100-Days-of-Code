from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data_set in question_data:
    question_bank += [Question(data_set["text"],data_set["answer"])]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextQuestion()

print("Your final score was: {}/{}".format(quiz.score,quiz.question_number))