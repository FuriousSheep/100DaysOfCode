class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def ask_question(self):
        print(self.text)
        answer = input("True or False?")
        if answer == self.answer:
            print("Correct!")
            return 1
        else:
            print("Wrong!")
            return 0