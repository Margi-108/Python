from question_store import load_questions,save_questions

# Load previously saved questions into json file
quiz_collection = load_questions()

def add_question():
    qid =  str(len(quiz_collection) + 1)
    question = input("Enter question : ")
    option1 = input("Enter option 1 : ")
    option2 = input("Enter option 2 : ")
    answer = input("Enter answer : ")

    quiz_collection[qid] = {
        "question" : question,
        "options" : [option1,option2],
        "answer" : answer
    }
    save_questions(quiz_collection)  
    
    print("\n  Question Added Successfully!!..... \n")

def view_question():
    if not quiz_collection:
        print(" Question is not available.")
        return
    
    for qid, qdata in quiz_collection.items():
        print(f"\n{qid} {qdata['question']}")
        print(f"A : {qdata['options'][0]}")
        print(f"B : {qdata['options'][1]}")
        print(f"Right Answer : {qdata['answer']} \n")
    
def delete_question():
    qid = input("Enter Question ID to delete : ")
    if qid in quiz_collection:
        confirm = input("Are you sure?? (Y/N) : ").upper()
        if confirm == 'Y':
            del quiz_collection[qid]
            save_questions(quiz_collection)  # delete question and save question in json file
            print(" Question Deleted!!.... ")
        else:
            print("Delete Canceled.... ")
    else:
        print("Invalid Question ID... ")

def master_menu():
    while True:
        print( "\n                               WELCOME MASTER ") 
        print("SHAKE YOUR BRAIN AND ADD SOME CHALLANGING QUESTIONS ... ")
        print( "\n                                          MENU  ") 
        print( "                               press 1 for add question ") 
        print( "                               press 2 for view questions ") 
        print( "                               press 3 for delete question ") 
        print( "                               press 4 exit ") 

        choice =int(input("Which operation do you want to perform : "))

        try:
            if choice == 1:
                add_question()
            elif choice == 2:
                view_question()
            elif choice == 3:
                delete_question()
            elif choice == 4:
                print("Exciting quiz master..... ")
                break
            else:
                print("Invalid Choice....")
        except ValueError:
            print("Invalid input. Please Enter Number only.")