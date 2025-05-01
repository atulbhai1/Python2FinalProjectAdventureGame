# ----------
# AdventureGame/WalmartJobPath/WalmartWinner.py
# ----------
# Description:
"""This file is the path the user can take after they win the minigame!"""
# ----------
# Created:
# 4/27/2025
# ----------
# Last Modified:
# 4/29/2025
# ----------
# Version #:
# 0.1
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.theend
import AdventureGame.jail
import time


def main():
    """This function adds points to the user's score, tells them that they won, and continues the story."""

    AdventureGame.universallyhelpfulthings.change_user_score_by(1000)#Add 1000 to the user's score for winning

    print("\nGreat Job!!! You've correctly identified everyone!!!")

    AdventureGame.universallyhelpfulthings.next_input("Talk to your manager")#Confirm that the user is ready to continue

    print("\nYour boss has a few words to say to you.“I see that you’re better than I thought. I’ll give you 2 options, I can give you the $50 you wanted, or I could let you join my venture capital team as a lie detector. You just need to detect lies and I’ll pay you a grand a day. What do ya say?”")

    user_path = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Accept his offer", "Decline his offer"])#Let the user accept or decline his offer

    if user_path == "Accept":#If the user accepted his offer
        print("You have reached a secret ending!")

        AdventureGame.universallyhelpfulthings.change_user_score_by(500)#This path is good, but not getting pie makes even riches just a minor benefit.

        AdventureGame.theend.main("You live a lavish life as a venture capitalist and retire rich in a mansion in Upstate New York. You never attain the salvation of a True American Apple Pie. \nThe End")
        return None#Leave this module, don't continue onwards

    #If the user didn't accept the offer, continue onwards in this module
    print("You are shortly kicked out of the room and are thrown $50. You pick yourself up and rush over to the bakery section, grab the ingredients, and buy your ingredients. In order to bake, you need to go to a kitchen to use an oven. You can break and enter into someone's house, or you can use the community kitchen oven.")

    user_path_2 = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Break and Enter", "Community Kitchen"])#Let the user choose their path

    if user_path_2 == "Break and Enter":#If the user chose to break and enter
        print("You find a home, break a window, and jump in. Just as you put the pie into the oven and begin to bake it, the police burst in and arrest you.\nGO TO JAIL!!!")

        AdventureGame.jail.main()#Send them to jail for breaking and entering
        return None#Leave this module, don't continue onwards

    #If the user made the wise choice not to break and enter, continue onwards in this module

    print("You go to your local community kitchen, get a nice meal, and decide to start baking. As you start, an old grandmother approaches you and offers to help. Do you accept?")

    user_path_3 = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Of course!", "No need"])#Does the user accept the grandmother's offer?

    if user_path_3 == "Of course!":#If they accepted
        print("The grandmother helps you greatly and works a bit of her magic to make a great pie. You bake it for 30 minutes.(Please wait 30 seconds)")
        time.sleep(30)#Wait 30 seconds
        print("You take a bite and it's...")
        AdventureGame.universallyhelpfulthings.next_input()#Increase suspense with pause
        #As this is a great ending, give them 2500 points!
        AdventureGame.universallyhelpfulthings.change_user_score_by(2500)
        #Send them to the end.
        AdventureGame.theend.main("AMAZING!!! A slice of true bliss; a True American Apple Pie. You share the slices with everyone you know and they are wowed. With that grandmother’s help, you go on to start a large company that mass produces True American Apple Pies, enlightening the world!\nThe End")
    else:#If they refused help
        print("The grandmother says, “Ok dear, good luck,” and goes away.")
        AdventureGame.universallyhelpfulthings.next_input()#Just confirm that they can continue
        print("As she goes away, you notice a tiny vial in her hand labeled anti-poison. Never minding that, you bake a pie that’s sure to be great. You bake it for 20 minutes.(Please wait 20 seconds")
        time.sleep(20)
        print("Then you take it out, cut out a small slice, take a bite, and it’s…")
        AdventureGame.universallyhelpfulthings.next_input()  # Increase suspense with pause
        print("TOXIC!!! The manager must have poisoned the ingredients!!!")
        AdventureGame.universallyhelpfulthings.change_user_score_by(-700)#Reduce the score more than the standard death penalty for the user having trusted Bob and having not accepted help.
        AdventureGame.theend.death()#Run the death function


# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
