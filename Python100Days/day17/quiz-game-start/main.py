from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_map = question_data[i]
    # we convert the data into an object and put it into a list to access its attributes easier
    question_bank.append(Question(text = question_map["question"], answer = question_map["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")