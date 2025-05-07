# ----------
# AdventureGame/WalmartJobPath/WalmartGame.py
# ----------
# Description:
"""This file is a game!!! It checks back with a .csv file to get people descriptions and classifications. It then gives the user 10 random people to decide whether
they are robbers are not. Even one mistake means the user loses!"""
# ----------
# Created:
# 4/26/2025
# ----------
# Last Modified:
# 4/27/2025
# ----------
# Version #:
# 0.1
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings
import os
import csv
import random
#-----------
#This is the path of the file we need to read from.
file_path = "WalmartGamePeople.csv"

def main():
    """This function is only really called from googleitWalmart.py . It is just a text game that will pull in people from a csv, randomly pick 10, and ask the user to correctly judge them."""

    #Change the current directory to Walmart Job Path if not already to access the WalmartGamePeople.csv file
    if str(os.getcwd())[-len("WalmartJobPath"):] != "WalmartJobPath":
        os.chdir(os.path.join(os.getcwd(), "WalmartJobPath"))#If the current directory isn't WalmartJobPath, it will be the parent of said directory

    #Load the csv into a list
    with open(file_path, "r") as WalmartGamePeople:
        GamePeople = list(csv.reader(WalmartGamePeople))

    used_game_people = GamePeople[1:]#Cut out the column names

    used_game_people = random.sample(used_game_people, k=10)#Randomly pick 10 entries from used_game_people

    #Let's pick a sorting algorithm by asking the user!
    print("Before we start the game, you need to help Atul! He needs to use both filter and map but can only use one at a time! Just reply with what is desired below:")

    algorithm = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Use filter()","Use map()"])

    print("Thanks!")

    #Have it separated just in case
    def filtering_fonc(person_choice_with_text:list, used_game_people):
        """This function uses the text(2nd element of the list) to cross-reference with the original chosen people list and return if the provided user input
        (1st element) is valid or not(Matches with what was expected?)."""

        for item in used_game_people:#For each entry
            if item[1] == person_choice_with_text[1]:#Check if this has the same description
                return item[0] == person_choice_with_text[0]#If so, return whether this is right or wrong
        return None#If no prior result, return none

    free_space = ["\n" for i in range(30)]#Use a list comprehension for the number of lines to print blank space just because

    for l in free_space:
        print(l)

    print("----------Starting Game------------")
    print("In this game, read the description and determine whether each person is a robber or if they are innocent. A single mistake means that you lose the game. Results are tallied after the game concludes.")

    person_choice = []
    for person in used_game_people:
        print(person[1])
        user_temp = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["INNOCENT", "ROBBER"])
        person_choice.append([user_temp] + [person[1]])#Use both .append() and list concatenation just because in order to add the user's choice and the attached description to the list of their choices

    user_won = True#By default, the user wins!

    if algorithm == "Use map()":#If they wanted to map results
        user_results = list(map(lambda x:filtering_fonc(x, used_game_people), person_choice))#Use map to make a list of True(Correct choices) and False(Wrong choices). Lambda was also incorporated just because

        if False in user_results:#If there was a single wrong answer
            user_won = False#User does not win!
    else:#They wanted to use filter
        user_results = list(filter(lambda x:filtering_fonc(x, used_game_people), person_choice))#Use filter to only select the user choices that are right(hopefully all 10). Lambda was also incorporated to push the dictionary of game people

        if len(user_results) < 10:#If not all 10 were correct
            user_won = False

    return user_won#Return whether the user won or lost as True or False







# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
