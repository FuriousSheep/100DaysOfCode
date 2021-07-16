from question_model import Question
from data import question_data as data

def main():
    questions = []
    score = 0
    max_score = 0

    for e in data:
        questions.append(Question(e["text"], e["answer"]))
    
    for question in questions:
        score += question.ask_question()
        max_score += 1
        print(f"Your score: {score}/{max_score}")

if __name__ == "__main__":
    main()
