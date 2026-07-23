questions = [
    ("What is the output of print(2 ** 3)?", "8"),
    ("Which keyword defines a function in Python?", "def"),
    ("What is the file extension for Python files?", "py"),
]
 
score = 0
print("Welcome to the Python Quiz!")
 
for question, answer in questions:
    print(f"Q: {question}")
    user_answer = input("Your answer: ").strip()
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The answer was: {answer}")
 
percentage = (score / len(questions)) * 100
print(f"You scored {score}/{len(questions)} — {percentage:.0f}%")
#hdfsjha