# ----------
# AdventureGame/MurderMysteryPath/findanexistingpieMurder.py
# ----------
# Description:
"""This file is the main file for the Murder Mystery pathway which the user can take by choosing to Find an Existing Pie."""
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

def main():
    """This function gives the user the start of a part of a story with choices and different paths. It is the Murder Mystery part of the game.
    It features a game in a different file and also diverges paths further into different files."""

    #Text introduction to this part of the story
    print("The best place to find a pie is not in a Walmart Bathroom, so you head out into the real world - the rest of the Walmart - and overhear someone saying: “My grandmother just made the best American Apple Pie! You should try some too when you come over!” You realize that if you follow them home, you could easily break in when they aren’t looking and steal the pie. What do you do?")

    #Let them choose to follow the same person or follow someone else
    user_choice = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Continue Following Them", "Follow someone else"])

    if user_choice == "Continue Following Them":#If they chose to continue following the ssme person
        pass

# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
