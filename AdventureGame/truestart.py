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
# 4/26/2025
#----------
#Version #:
#0.3
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.WalmartJobPath.googleitWalmart
import AdventureGame.credits
#----------



def main():
    """This function gives the user an introduction to the game and gives them options they can take. It will be one of the major crossroads of the game. User score
    is required to calculate the final score and to push to called functions beyond. os_type is similar but needed for imports.
    *An extra backdoor is inbuilt to show a secret area."""

    print("""Start of Adventure: The True American Apple Pie
    
You have decided to embark on a dangerous quest to get a coveted True American Apple Pie.
You have several paths you can take on this perilous journey.\n""")

    choices = ["Google It", "Find an Existing Pie", "Leave The Game(W/ Credits and Dev. Info)"]

    user_chosen = universallyhelpfulthings.multiple_choice_input_collection(choices)
    if user_chosen == "Google It":
        AdventureGame.WalmartJobPath.googleitWalmart.main()#Go to the Walmart part of the game
    elif user_chosen == "Leave The Game(Skip to Credits and Dev. Info)":
        print("Leaving...")

    AdventureGame.credits.main()#Show credits


#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
