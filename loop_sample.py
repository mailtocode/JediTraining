import random

questions = []

done = False

while not done:
    a_question = input("Enter a question: ")
    answers = []

    for index in range(4):
        a_answer = input("Enter a answer: ")
        correct_str = input("Is this a correct answer? (y/n): ")
        correct = True if correct_str == "y" else False
        answers.append((a_answer, correct))

    questions.append((a_question, answers))

    done_str = input("Are you done with all questions? (y/n): ")
    done = True if done_str == "y" else False

random.shuffle(questions)

for element in questions:
    (question_item, answer_items) = element
    print(question_item)
    random.shuffle(answer_items)
    for answer_item in answer_items:
        (s_answer,is_correct) = answer_item
        print(f"----{s_answer} - {is_correct}")

