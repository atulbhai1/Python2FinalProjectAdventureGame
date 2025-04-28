# ----------
# AdventureGame/WalmartJobPath/WalmartWinner.py
# ----------
# Description:
"""This file is the path the user can take after they win the minigame!"""
# ----------
# Created:
# 4/27/2025
# ----------
# Last Modified:
# 4/27/2025
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
    """This function adds points to the user's score, tells them that they won, and continues the story."""

    AdventureGame.universallyhelpfulthings.change_user_score_by(1000)#Add 100 to the user's score

    print("\nGreat Job!!! You've correctly identified everyone!!!")

    AdventureGame.universallyhelpfulthings.next_input("Talk to your manager")#Confirm that the user is ready to continue







# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
