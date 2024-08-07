from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
length = len(question_data)
question_bank = []
for item in question_data:
    question_text = item['text']
    question_answer = item['answer']
    new_Question = Question(question_text, question_answer)
    question_bank.append(new_Question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You have completed the quiz")
print(f"Final score is {quiz.score}/ {len(question_bank)}")
