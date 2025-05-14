#----------
#AdventureGame/restart.py
#----------
#Description:
"""This file is the restarting point for the user for this entire project.
They will be given several options and redirected from here.
This file is forwarded to many times"""
#----------
#Created:
# 5/3/2025
#----------
#Last Modified:
# 5/3/2025
#----------
#Version #:
#0.0
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.WalmartJobPath.googleitWalmart
import AdventureGame.theend
import AdventureGame.MurderMysteryPath.findanexistingpieMurder
import AdventureGame.LandOfPiPiesPath.askforhelpPiPies
#----------



def main():
    """This function gives the user a reminder to the game's purpose and gives them options they can take. It will be one of the major crossroads of the game.
    *An extra backdoor is inbuilt to show a secret area."""

    print("You’re back where you started: you still want a True American Apple Pie. Which path will you take?\n")

    choices = ["Google It", "Find an Existing Pie", "Ask for help","Leave The Game(Skip to End From Here)"]

    user_chosen = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(choices)#Get their path choice

    #Redirect them based off their choice
    if user_chosen == "Google It":
        AdventureGame.WalmartJobPath.googleitWalmart.main()#Go to the Walmart part of the game
    elif user_chosen == "Find an Existing Pie":
        AdventureGame.MurderMysteryPath.findanexistingpieMurder.main()#Go to the murder mystery part of the game
    elif user_chosen == "Ask for help":
        AdventureGame.LandOfPiPiesPath.askforhelpPiPies.main()
    elif user_chosen == "Leave The Game(Skip to End From Here)":
        print("Leaving...")

        AdventureGame.theend.main("You skipped here")

        if input("(Press Enter To End)") == "SECRETBACKDOOR!!!":
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
