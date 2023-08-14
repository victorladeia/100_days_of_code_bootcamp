from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

list_of_questions = []

for question in question_data:
    list_of_questions.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(list_of_questions)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
