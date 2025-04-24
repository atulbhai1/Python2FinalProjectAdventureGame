#----------
#AdventureGame/truestart
#----------
#Description:
"""This file is the starting point for the user for this entire project.
They will be given several options and redirected from here."""
#----------
#Created:
# 4/23/2025
#----------
#Last Modified:
# 4/23/2025
#----------
#Version #:
#0.0
#----------
#Interpreter:
#Python 3.11
#----------
#Imports

#----------
#Universal Variables used throughout the game
#They're declared after imports to ensure that the declaration of those variables in the custom modules for testing doesn't override these
user_score = 0#The user starts with 0 points in the scoring system

def main():
    """This function pushes the user to the start page and deals with any exceptions that aren't covered
    by the rest of the program."""
    global user_score#Required to make it redefinable for the functions to be called.
    pass

#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
