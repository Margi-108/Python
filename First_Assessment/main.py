from quiz_master import master_menu
from quiz_cracker import play_quiz

def main():
    while True:
        print( "                               WELCOME TO TOPS QUIZ GAMING CHALLANGE ") 
        print("\n                               SELECT YOUR ROLE :          ")
        print("\n                                      -> QUIZ MATSER  (PRESS 1 )"  )
        print("                                      -> QUIZ CRACKER  (PRESS 2 )" )
        print("                                      -> Exit  (PRESS 3 )" )

        role = int(input("\n\n ENTER YOUR ROLE :  "))

        try:
            if role == 1:
                master_menu()
            elif role == 2:
                play_quiz()
            elif role == 3:
                print("Exciting QUIZ GAME.....")
                break
            else:
                print("Invalid choice....")
        except ValueError:
            print("Invalid input. Please Enter Number Only.")
        
main()
