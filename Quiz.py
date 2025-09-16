# List of questions (dictionary format)
quiz_questions = [
    {"question": "Q1: Capital of India?", "answer": "delhi"},
    {"question": "Q2: 5 + 7 = ?", "answer": "12"},
    {"question": "In which year did India gain independence?", "answer": "1947"},
    {"question": "Which is the largest continent by area?", "answer": "asia"},
    {"question": "Which river is known as the longest in the world?", "answer": "nile"},
    {"question": "Which ocean is the deepest?", "answer": "pacific"},
    {"question": "Q3: Python is programming language? (yes/no)", "answer": "yes"}
]

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q["question"])
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")
    return score

score = run_quiz(quiz_questions)
percentage = (score / len(quiz_questions)) * 100
print(f"✅ Your Score: {score}/{len(quiz_questions)} ({percentage:.2f}%)")
