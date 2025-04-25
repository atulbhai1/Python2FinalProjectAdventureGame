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
# 4/24/2025
#----------
#Version #:
#0.1
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import universallyhelpfulthings
import WalmartJobPath.googleitWalmart
#----------
#Universal Variables used throughout the game


def main(user_score, os_type):
    """This function gives the user an introduction to the game and gives them options they can take. It will be one of the major crossroads of the game. User score
    is required to calculate the final score and to push to called functions beyond. os_type is similar but needed for imports.
    *An extra backdoor is inbuilt to show a secret area."""

    print("""Start of Adventure: The True American Apple Pie
    
You have decided to embark on a dangerous quest to get a coveted True American Apple Pie.
You have several paths you can take on this perilous journey.\n""")

    choices = ["Google It", "Find an Existing Pie", "Leave The Game(W/ Credits and Dev. Info)"]

    user_chosen = universallyhelpfulthings.multiple_choice_input_collection(choices)
    if user_chosen == "Google It":
        WalmartJobPath.googleitWalmart.main(user_score, os_type)
    elif user_chosen == "Leave The Game(W/ Credits and Dev. Info)":
        print("Leafing")
        print(user_score+100)

#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main(0, "dt")
