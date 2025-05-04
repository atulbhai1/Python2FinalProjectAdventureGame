# ----------
# AdventureGame/LandOfPiPiesPath/askforhelpPiPies.py
# ----------
# Description:
"""This file is the main file for the Land of Pi Pies pathway which the user can take by choosing to Ask for help."""

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
import AdventureGame.jail
import AdventureGame.LandOfPiPiesPath.PiofPieQuiz

def main():
    """This function gives the user the start of a part of a story with choices and different paths. It is the Land of Pi Pies part of the game.
    It just has a few dialogue parts that redirect further."""

    print("\nYou ask around for help finding a True American Apple Pie, and are given two offers. Bob -your store manager- offers to help take you to the land of Pi Pies to find 3.14159265… True American Apple Pies. Meanwhile, a green midget with a giant green head and large plain black eyes offers to help you search for a True American Apple Pie in space. Which offer do you accept?")

    #Let the user pick who to trust
    user_path = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Green Midget", "Bob"])

    if user_path == "Green Midget":
        print("The green midget takes you to a giant tree and jumps into a hole at the base of said tree. He implores you to follow him. Do you jump now, wait a few seconds, or go to the store manager?")

        # Let the user pick their path
        user_path_2 = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Wait", "Jump Now", "Go to Bob"])

        if user_path_2 == "Jump Now":#If they wanted to jump now
            AdventureGame.universallyhelpfulthings.change_user_score_by(300)#Trusting aliens is good, so reward them
            print("The green midget says, “You have passed your test of trust. Let me be truthful now: I’m a being of a different planet than your own and have no clue what a True American Apple Pie is. Regardless, I am determined to help you. I can take you to the world of Pi Pies and maybe you will find help there.”")

            AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

            print("You feel a strange vibration under your feet and see a window appear. From the window, you can see that the ground is getting farther and farther away and that you’re quickly approaching space. Just a few minutes later, the tree lands down on a land covered in pies. You realize that you are now in…")

            AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

            the_land_of_pi_pies()#Send them to the_land_of_pi_pies() to continue the story
        elif user_path_2 == "Go to Bob":#If they wanted to just go to Bob instead
            go_to_bob()#Send them to Bob!
        else:#If they chose to wait
            AdventureGame.universallyhelpfulthings.change_user_score_by(-500)#Hesitating to trust aliens is very bad, so penalize them a bit more
            print("The green midget says, “Hurry up! We’re about to leave without you!” Hearing this, you quickly jump in and land on a metal table. Before you can get up, you feel metal grips grabbing your hands and legs.")

            AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

            print("The green midget speaks, “You didn’t trust me did you? It’s time for you to pay for your lack for trust in a superior species. I’ll cut you up and feed you to my woc!”")

            AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

            print("A rotating blade turns on and begins approaching your head. You close your eyes and brace. It hurts for the first second, but soon afterwards…")

            AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

            AdventureGame.theend.death()#They died, so redirect them accordingly

    else:#If they originally chose to accept Bob's help
        go_to_bob()#Send them to Bob

def go_to_bob():
    """This helps consolidate players on the 2 possible routes before redirecting them further to the_land_of_pi_pies()."""

    AdventureGame.universallyhelpfulthings.change_user_score_by(-300)#Bob is bad, so penalize them

    print("Bob the store manager takes you into his office and says, “Ha! I knew you were as gullible as I thought you were! Now you’re going to be trapped in the land of Pi Pies!”")

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    print("The next second, the walls around you seem to collapse and Bob disappears. You realize that you are now in …")

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    the_land_of_pi_pies()#Send them to the_land_of_pi_pies() to continue

def the_land_of_pi_pies():
    """This is a good chunk of the storyline. It consolidates the paths and takes the user to the great Pi of Pie."""

    print("The land of Pi Pies!")

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    print("You walk out a bit and are quickly confronted by a pie. It says, “Welcome to the land of Pi Pies. We are ruled by the great king, Pi Pie. Our favorite holiday is Pi day and we have many, many rules that need to be followed. Two guides will help you ahead, but beware, only one tells the truth!”")

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    print("You walk a few hundred feet along the dirt path and are confronted by 2 other pies. One pie says, “Hello, I’m Bob Pieson! I’m always telling the truth!” The other says, “Hello, I’m Jack Pier! I always try my best to be truthful, but I am just a pie.” Which pie do you take to be your guide?")

    #Let the user pick who will guide them
    user_guide = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Jack", "Bob"])

    if user_guide == "Jack":#If they wanted Jack to be their guide
        AdventureGame.universallyhelpfulthings.change_user_score_by(500)#Jacks are great! Reward them for this choice!
        print("Jack speaks to you, “Great! Just follow the red road, help all those along the way, and remember to use radians for everything!")
    else:#If they picked Bob to be their guide
        AdventureGame.universallyhelpfulthings.change_user_score_by(-500)#Never trust a Bob! Punish them for this choice!
        print("Bob speaks to you, “Great! Just follow the yellow road, realize that all of those along the way are evil, and remember to use degrees for everything!")

    #Regardless of their guide, they should see the following

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    print("You take the road, carefully following all of their recommendations, seeing a ScarePie, a Pion, and a Man of Pie. You also kill the evil Pie Witch of the west and befriend a piog named Pipo.")

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    print("You reach the house of the great king, Pi Pie and are given a slot to see him. After an hour of waiting, he summons you in…")

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    print("The great Pi Pie sits upon a throne of flour, eggs, sugar, and fruit and says, “Hello great adventurer. I see the things you have done and know of why. Just answer a few questions correctly to receive your reward or be executed for your failure.”")

    AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

    print("The great Pi Pie asks, “Did you help everyone along the way to the best of your ability?”")

    #Let them decide whether or not they helped others
    user_helped_others = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Yes", "No"])

    if user_helped_others == "Yes":#If the user helped others
        AdventureGame.universallyhelpfulthings.change_user_score_by(700)#Helping others is a good thing to do. Reward them!

        print("The great Pi Pie says, “I see that you are a very kindhearted and wholesome person. Just answer the following questions correctly to avoid execution and receive your prize.”")

        AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

        AdventureGame.LandOfPiPiesPath.PiofPieQuiz.main()#Send them to the quiz

    else:#If they didn't help others
        AdventureGame.universallyhelpfulthings.change_user_score_by(-600)#not helping others is a bad thing. Punish them!

        print("The great Pi Pie turns to his royal assistant and whispers some words into his piear. He turns and speaks, “I see that your values don’t quite align with mine, so I’ve arranged for your safe transfer to a prison on your home planet.")

        AdventureGame.universallyhelpfulthings.next_input()  # Let them continue with a next input

        AdventureGame.jail.main()#Send them to jail




# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()

#NOTE: There is only one file in this folder because of just how interconnected this path is and how small each of the sections are.