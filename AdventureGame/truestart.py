#----------
#AdventureGame/truestart.py
#----------
#Description:
"""This file is the starting point for the user for this entire project.
They will be given several options and redirected from here."""
#----------
#Created:
# 4/23/2025
#----------
#Last Modified:
# 5/3/2025
#----------
#Version #:
#0.5
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.WalmartJobPath.googleitWalmart
import AdventureGame.credits
import AdventureGame.MurderMysteryPath.findanexistingpieMurder
import AdventureGame.LandOfPiPiesPath.askforhelpPiPies
#----------



def main():
    """This function gives the user an introduction to the game and gives them options they can take. It will be one of the major crossroads of the game.
    *An extra backdoor is inbuilt to show a secret area."""

    print("""Start of Adventure: The True American Apple Pie
    
You have decided to embark on a dangerous quest to get a coveted True American Apple Pie.
You have several paths you can take on this perilous journey.\n""")

    choices = ["Google It", "Find an Existing Pie", "Ask for help","Leave The Game(Skip to Credits and Dev. Info)"]

    user_chosen = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(choices)#Get their path choice

    #Redirect them based off their choice
    if user_chosen == "Google It":
        AdventureGame.WalmartJobPath.googleitWalmart.main()#Go to the Walmart part of the game
    elif user_chosen == "Find an Existing Pie":
        AdventureGame.MurderMysteryPath.findanexistingpieMurder.main()#Go to the murder mystery part of the game
    elif user_chosen == "Ask for help":
        AdventureGame.LandOfPiPiesPath.askforhelpPiPies.main()#Go to the land of pi pies part of the game
    elif user_chosen == "Leave The Game(Skip to Credits and Dev. Info)":
        print("Leaving...")

        AdventureGame.credits.main()#Show credits

        if input("(Press Enter To End)") == "SECRETBACKDOOR!!!":#If they wanted to get to the secret backdoor
            print("Welcome to this secret area. This is a nice area. Here is a plant I made.")
            print("""
   \|||/
   -| |-
   /|||\\
     |
     |
     |
   -----
   \   /
    ---
""")
            print("I like this plant.")
            print("---Fin.---")


#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
