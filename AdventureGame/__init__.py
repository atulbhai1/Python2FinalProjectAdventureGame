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
# 4/24/2025
#----------
#Version #:
#0.2
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import os#Needed for os details to be used for importing files
import truestart#Will be called
#----------
#Universal Variables used throughout the game
#They're declared after imports to ensure that the declaration of those variables in the custom modules for testing doesn't override these
user_score = 0#The user starts with 0 points in the scoring system
os_type = os.name#Needed as I will need to use a backslash for Windows while I need to use a normal dividing sign for Mac or Linux


def main():
    """This function pushes the user to the start page and deals with any exceptions that aren't covered
    by the rest of the program."""
    global user_score#Required to make it redefinable for the functions to be called.
    try:
        truestart.main(user_score, os_type)
    except BaseException as e:
        print("Sadly an unknown error occurred!!!")
        print("Error details:")
        print(e)

#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
