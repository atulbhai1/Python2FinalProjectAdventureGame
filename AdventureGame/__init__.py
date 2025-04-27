#----------
#AdventureGame/__init__.py
#----------
#Description:
"""This file is the central file of this adventure game and will merely serve as a central hub to be a high level
gateway to other files in this package."""
#----------
#Created:
# 4/22/2025
#----------
#Last Modified:
# 4/25/2025
#----------
#Version #:
#0.3
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.truestart#Will be called
import AdventureGame.universallyhelpfulthings#For user_score
#----------
AdventureGame.universallyhelpfulthings.user_score_redefinition(0)#Reset the user's score to 0

def main():

    """This function pushes the user to the start page and deals with any exceptions that aren't covered
    by the rest of the program."""
    try:
        truestart.main()
    except BaseException as e:
        print("Sadly an unknown error occurred!!!")
        print("Error details:")
        print(e)

#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
