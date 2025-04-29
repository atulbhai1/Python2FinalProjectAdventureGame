#----------
#AdventureGame/jail.py
#----------
#Description:
"""This file is a central meeting point for the whole project. There are several pathways that end up in jail, making this rather important. It also has a game in case one wants to escape jail!"""
#----------
#Created:
# 4/28/2025
#----------
#Last Modified:
# 4/28/2025
#----------
#Version #:
#0.0
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.theend
import time
#----------

def main(message):
    """This function just reduces the player's score, tells them that they're in jail, and lets them either wait it out or play a game to escape(Forwards to other func.)."""

    AdventureGame.universallyhelpfulthings.change_user_score_by(-1000)#Jail is bad, so remove a lot of points!

    print("You're in JAIL!!!! What now?")

    user_choice = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Escape!!!", "Wait out your sentence"])#Get the user's choice

    if user_choice == "Wait out your sentence":#If they wanted to wait it out
        print("You decide to wait out the entirety of your prison sentence, an unbelievably long 30 seconds.")
        time.sleep()

def death():
    """This function is used by other modules when the user dies. It calls main() with a specific message and changes the user score."""

    message_for_death = "YOU DIED!!!"

    AdventureGame.universallyhelpfulthings.change_user_score_by(-2000)#Death is a big downside, remove 2000 points from the user's score.

    main(message_for_death)


#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main("U DED!!!")
