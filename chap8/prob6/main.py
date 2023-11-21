import random

def load_questions(filet):
    questions = []
    for filet in filet:
        with open(filet, 'r') as file:
            lines = file.read().split('\n')
            question = {
                'question': lines[0][3:].strip(),
                'answers': [line[3:].strip() for line in lines[1:4]],
                'correct_answer': lines[4][0].strip(), 
            }
            questions.append(question)
    return questions

def trivia_game(questions):
    random.shuffle(questions)
    for question in questions:
        print("\n-------------")
        print(question['question'])
        for i, answer in enumerate(question['answers'], start=1):
            print(f"{i}. {answer}")
        user_answer = input("\nEnter your answer (1, 2, 3): ")
        if user_answer == question['correct_answer']:
            print("correct answer!")
        else:
            print(f"wrong answer! correct answer : {question['correct_answer']}.")

if __name__ == "__main__":
    question_files = ["Q1.txt", "Q2.txt", "Q3.txt", "Q4.txt"]
    trivia_questions = load_questions(question_files)
    trivia_game(trivia_questions)
