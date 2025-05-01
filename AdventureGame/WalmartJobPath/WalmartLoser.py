# ----------
# AdventureGame/WalmartJobPath/WalmartLoser.py
# ----------
# Description:
"""This file is the path the user can take after they lose the minigame!"""
# ----------
# Created:
# 4/29/2025
# ----------
# Last Modified:
# 4/29/2025
# ----------
# Version #:
# 0.0
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.jail


def main():
    """This function removes points to the user's score, tells them that they lost, and continues the story."""

    AdventureGame.universallyhelpfulthings.change_user_score_by(-1000)#Remove 1000 from the user's score for losing

    print("\nYou've failed! Loser!!!")

    AdventureGame.universallyhelpfulthings.next_input("Talk to your manager")#Confirm that the user is ready to continue

    print("\nYour boss has a few words to say to you. “Ha! I see that you’re the failure I knew you were! I’m not giving you a penny for the trash you did! You’re lucky I’m letting you stay in the stalls at night! You think I don’t know? I know everything under my domain. Now, shoo! I don’t wanna see you ever again!”")

    user_path = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Rob the ingredients", "Give up on this for now"])#Let the user give up or rob ingredients

    if user_path == "Give up on this for now":#If the user gave up
        # AdventureGame.restart.main()
        pass
    else:#If they chose to rob the ingredients

        print("You sneak away to the bakery section, take the ingredients, and hide them under your shirt. As you try to leave the store…")
        AdventureGame.universallyhelpfulthings.next_input()#Confirm that the user is ready to continue
        print("Nobody confronts you and you sigh with relief. But as you go across the parking lot…")
        AdventureGame.universallyhelpfulthings.next_input()#Confirm that the user is ready to continue
        print("The store security officer chases you with a gun and threatens to shoot. With his gun on your back, he calls the police and they take you away. GO TO JAIL!!!")
        AdventureGame.jail.main()#Go to jail!

# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
