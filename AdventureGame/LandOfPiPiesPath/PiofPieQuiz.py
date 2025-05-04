# ----------
# AdventureGame/LandOfPiPiesPath/PieofPieQuiz.py
# ----------
# Description:
"""This file is the 5 question quiz which needs to be filled out correctly for the player to win."""

# ----------
# Created:
# 5/3/2025
# ----------
# Last Modified:
# 5/3/2025
# ----------
# Version #:
# 0.0
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.theend
import random
import os
import csv


def main():
    """This function reaches into a csv to get questions, rearranges the data to make it useful, randomly picks questions, asks the user, and redirects them after they have answered 5 questions depending on their accuracy."""

    print("In this game, you have to answer 5 out of 5 multiple choice questions correctly to win.")

    AdventureGame.universallyhelpfulthings.next_input("Start")#make sure that they are ready to start

    all_correct = True#By default, the user has 100% accuracy.

    # Data preparation

    # Change the current directory to LandOfPiPiesPath if not already to access the PiOfPieQuestions.csv file
    if str(os.getcwd())[-len("LandOfPiPiesPath"):] != "LandOfPiPiesPath":
        os.chdir(os.path.join(os.getcwd(), "LandOfPiPiesPath"))  # If the current directory isn't LandOfPiPiesPath, it will be the parent of said directory

    #Load the csv into a list
    with open("PiOfPieQuestions.csv", "r") as questions_file:
        questions = list(csv.reader(questions_file))

    #Add questions to a new list with each question formatted like {question, correct_answer, all possible answers}
    usable_questions = []
    for question in questions[1:]:
        usable_questions.append({"Question":question[0], "Correct Answer":question[1], "ALL Possible Answers":question[1:]})

    used_questions = random.choices(usable_questions, k=5)#Pick 5 random questions to show

    #Now we're ready to begin!

    print("---Starting Test---")

    #For each question, print out the question prompt and get the user's answer from the multiple possible answers.
    # Then check if their answer was not right and change the all_correct variable accordingly
    for question in used_questions:
        print("\nQuestion:", question["Question"])

        #Remember to scramble the order of the answer choices! Remember that random.shuffle modifies the original list!
        random.shuffle(question["ALL Possible Answers"])

        user_answer = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(question["ALL Possible Answers"])

        if user_answer != question["Correct Answer"]:
            all_correct = False

    #They're done now!
    if all_correct:#If all the responses were correct
        print("You did it! You answered all 5 questions correctly!")
        AdventureGame.universallyhelpfulthings.change_user_score_by(2500)#For having won a great victory and having secured a lifetime of pie, give them points
        AdventureGame.universallyhelpfulthings.next_input()  # make sure that they are ready to continue

        print("The great Pi Pie speaks, “You have done wonderful. I am impressed. I shall arrange for a great award for your triumph.”")

        AdventureGame.universallyhelpfulthings.next_input()  # make sure that they are ready to continue

        #Send them to the end
        AdventureGame.theend.main("You are soon given a great estate by the house of the great Pi Pie and serve as a reputed courtier in his court. You are granted access to as many True American Apple Pies as any man could ever wish for and live a long, happy, and contented life under the generous Pi Pie.\nThe End")
    else:#If not all the responses were correct
        print("Not all of your answers were correct. YOU LOST!!!")
        AdventureGame.universallyhelpfulthings.next_input(-1200)#The Great Pi of Pie is rather angry at the user having lost. So remove some points
        AdventureGame.universallyhelpfulthings.next_input()  # make sure that they are ready to continue

        print("The great Pi Pie speaks, “How dare you fail to pass this simple test of our truths! There is only one place you belong…")

        AdventureGame.universallyhelpfulthings.next_input()  # make sure that they are ready to continue

        print("The underworld!”")

        AdventureGame.universallyhelpfulthings.next_input()  # make sure that they are ready to continue

        AdventureGame.theend.death()#They die!!!

# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()

#NOTE: There is only one file in this folder because of just how interconnected this path is and how small each of the sections are.