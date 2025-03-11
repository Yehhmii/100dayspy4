from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_model in question_data:
    question_text = q_model["text"]
    question_answer = q_model["answer"]
    current_questions = Question(question_text, question_answer)
    question_bank.append(current_questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your finial score was: {quiz.score}/{quiz.question_number}")
