#----------
#AdventureGame/theend.py
#----------
#Description:
"""This file is the end of the project. It will display a message, show you information about your points, and that's all!"""
#----------
#Created:
# 4/28/2025
#----------
#Last Modified:
# 4/28/2025
#----------
#Version #:
#0.0
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.credits
#----------

#Save the rankings and the attached conditions(lambda) as a dictionary
points_rankings = {"Loser": lambda x: x <= 0, "Junior": lambda x: 0 < x <= 500, "Casual": lambda x: 500 < x <= 1300, "Expert": lambda x: x>1300}

def main(message):
    """This function just displays a message and concludes the story. The user's final score is displayed alongside a ranking of their score."""

    print(message)#Display the message passed to this function

    print("-----THE END-----")

    print("Here's how many points you have:")

    number_of_points = AdventureGame.universallyhelpfulthings.user_score_retrieval()#Save the number of points the user has

    print("You have:", number_of_points, "Points")

    user_ranking = None

    for ranking, condition in points_rankings.items():#Unpack the .items() TUPLES(YAY!!!) from the dict to compare with the user score
        if condition(number_of_points):#If the condition is met with this score
            user_ranking = ranking#The user has this ranking
            break#Leave this loop! No more comparisons required

    print("That means that you are a(n)", user_ranking)#Tell the user what ranking they are.

    print("\nThank you for playing, hope you play again!")

    AdventureGame.credits.main()#Send them to the credits section

def death():
    """This function is used by other modules when the user dies. It calls main() with a specific message and changes the user score."""

    message_for_death = "YOU DIED!!!"

    AdventureGame.universallyhelpfulthings.change_user_score_by(-2000)#Death is a big downside, remove 2000 points from the user's score.

    main(message_for_death)


#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main("U DED!!!")
