# ----------
# AdventureGame/WalmartJobPath/googleitWalmart.py
# ----------
# Description:
"""This file is a game!!! It checks back with a .csv file to get people descriptions and classifications. It then gives the user 10 random people to decide whether
they are robbers are not. Even one mistake means the user loses!"""
# ----------
# Created:
# 4/26/2025
# ----------
# Last Modified:
# 4/26/2025
# ----------
# Version #:
# 0.0
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings
import os
import csv
#-----------
#This is the path of the file we need to read from.
file_path = "WalmartGamePeople.csv"

def main():
    """This function is only really called from googleitWalmart.py . It is just a text game that will pull in people from a csv, randomly pick 10, and ask the user to correctly judge them."""
    pass



# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
