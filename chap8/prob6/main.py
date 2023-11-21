import random

# Load questions from files
questions = []
for file_path in ["Q1.txt", "Q2.txt", "Q3.txt", "Q4.txt"]:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
        question = {
            'question': lines[0][3:].strip(),
            'answers': [line[3:].strip() for line in lines[1:4]],
            'correct_answer': lines[4][3:].strip(),
        }
        questions.append(question)

# Shuffle questions
random.shuffle(questions)

# Play trivia game
for question in questions:
    print("\n-------------")
    print(question['question'])
    for i, answer in enumerate(question['answers'], start=1):
        print(f"{i}. {answer}")
    user_answer = input("\nEnter your answer (1, 2, or 3): ")
    if question['answers'][int(user_answer) - 1] == question['correct_answer']:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {question['correct_answer']}")
