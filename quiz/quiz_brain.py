class QuizBrain:

    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_list[self.question_number:] != []
    
    def check_answer(self, user_answer, correct_answer) -> bool:

        if correct_answer.casefold() == user_answer.casefold():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print("The correct answer was: {}".format(correct_answer))
        print("Your currect score is: {}/{}\n".format(self.score, self.question_number+1))

    def nextQuestion(self):
        answer = input("Q.{}: {} (True/False)?: ".format(self.question_number + 1, self.question_list[self.question_number].text))
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1