class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.question_bank = question_bank
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """Asks a question, increases score is the answer was right, 
        and increases the question number"""
        question = self.question_bank[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number} {question.text} (True/False)?")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        """Returns true if there are still questions, false if not"""
        return len(self.question_bank) > self.question_number

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer was: {question_answer}")
        print(f"Your score: {self.score}/{self.question_number}\n")
