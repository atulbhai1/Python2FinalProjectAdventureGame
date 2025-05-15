#----------
#playAdventureGame.py
#----------
#Description:
"""This file just runs AdventureGame."""
#----------
#Created:
# 5/3/2025
#----------
#Last Modified:
# 5/14/2025
#----------
#Version #:
#0.1
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame
#----------

main = AdventureGame.main#Reassign a function to have another name!

password = "AtulIsCool1234"

#Standard practice, if this file is being run on its own(as it needs to be), get the password sign in and run main()
if __name__ == "__main__":
    user_password_entry = input("Welcome to Atul's Adventure Game! Enter your password to start:")#Get the user to enter a password to begin

    if password == user_password_entry:  # If they entered the right password
        repeat = True#By default, keep playing this game forever!!!
        while repeat:#While it should repeat
            print()
            main()
            user_choice = input("Thanks for playing. Want to play AGAIN???(Enter 'Y' to play again, or enter anything else to leave)")
            if user_choice.lower().strip() != 'y':#If they didn't choose to continue
                repeat = False#Stop looping
                print("Goodbye, please return to this wonderful game sooner rather than later.")
                #--Fin.--
            #If they did choose to continue, it will automatically as repeat is True by default
    else:#Password entered is wrong
        print("You shouldn't be here. You've been very very bad.")

        #--Fin.--



