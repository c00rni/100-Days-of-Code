from question_model import Question
from data import QuestionGenerator
from quiz_brain import QuizBrain
from html import unescape
from ui import QuizzlerUI

question_bank = []
questions = QuestionGenerator().getQuestions()
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(unescape(question_text), question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
QuizzlerUI(quiz)
#while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
