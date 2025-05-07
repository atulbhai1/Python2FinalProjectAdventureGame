#----------
#AdventureGame/__init__.py
#----------
#Description:
"""This file is the starting file of this adventure game and will merely serve as a starting point that configures one thing, handles exceptions, and redirects to the true start."""
#----------
#Created:
# 4/22/2025
#----------
#Last Modified:
# 5/3/2025
#----------
#Version #:
#0.4
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.truestart#Will be called
import AdventureGame.universallyhelpfulthings#For user_score
#----------
AdventureGame.universallyhelpfulthings.user_score_redefinition(0)#Reset the user's score to 0
#Also, this changes the working directory to AdventureGame, which is nice & needed to access files later on

def main():

    """This function pushes the user to the start page and deals with any exceptions that aren't covered
    by the rest of the program."""
    try:
        AdventureGame.truestart.main()
    except BaseException as e:
        print("Sadly an unknown error occurred!!!")
        print("Error details:")
        print(e)

#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()

#Extra Note Section

#There are a few characters
#The store manager is an evil, murdering, sociopath.
#Anyone named Bob is inherently bad.
#The person in the stall over is good
#Aliens are good
#The Great Pi of Pie is a strict but benevolent and generous ruler

#I used as many things as I could in Python.
#My class is in universally helpful things and is the custom exception for invalid inputs
#I used a method of that class for the error message

#My storyline gets broken up based on user input but works towards a universal goal