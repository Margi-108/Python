from question_store import load_questions


def play_quiz():
    quiz_collection = load_questions()
    score = 0

    if not quiz_collection:
        print("Question is not display..")
        return
    
    for qid, qdata in quiz_collection.items():
        print(f"{qdata['question']}")
        print(f"A : {qdata['options'][0]}")
        print(f"B : {qdata['options'][1]}")

        user_ans = input("Enter Your Answer : ").strip()
        if user_ans.lower() == qdata['answer'].lower():
            print(" Correct Answer!!...\n")
            score += 1
        else:
            print(f"Wrong!! . Correct Answer is : {qdata['answer']}\n")

    print(f"QUIZ COMPLETED... Your score is : {score} out of {len(quiz_collection)}\n")