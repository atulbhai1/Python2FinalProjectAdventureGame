# ----------
# AdventureGame/MurderMysteryPath/findanexistingpieMurder.py
# ----------
# Description:
"""This file is the main file for the Murder Mystery pathway which the user can take by choosing to Find an Existing Pie."""
from pygame.key import start_text_input

# ----------
# Created:
# 4/29/2025
# ----------
# Last Modified:
# 5/1/2025
# ----------
# Version #:
# 0.1
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings
from datetime import datetime, timedelta

def main():
    """This function gives the user the start of a part of a story with choices and different paths. It is the Murder Mystery part of the game.
    It features a game in a different file and also diverges paths further into different files."""

    #Text introduction to this part of the story
    print("The best place to find a pie is not in a Walmart Bathroom, so you head out into the real world - the rest of the Walmart - and overhear someone saying: “My grandmother just made the best American Apple Pie! You should try some too when you come over!” You realize that if you follow them home, you could easily break in when they aren’t looking and steal the pie. What do you do?")

    #Let them choose to follow the same person or follow someone else
    user_choice = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Continue Following Them", "Follow someone else"])

    if user_choice == "Continue Following Them":#If they chose to continue following the ssme person
        continue_following_them()#Continue following them in a different function
    else:#They choose to follow someone else
        follow_someone_else()#Follow someone else in a different function

def continue_following_them():
    """This function is just what happens in one path. It just has a few paths within it that all lead towards the same ending. Only one path leads somewhere else. A minigame is also referenced."""

    print("You follow them to their car and manage to overhear that they live just 3 miles away in a nice neighborhood. You also manage to get their exact address. You have several choices to follow them now.")

    #Get their choice of transport option
    user_transportation_option = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Take The Bus", "Walk", "Go on/in their car"])

    if user_transportation_option == "Take The Bus" or user_transportation_option == "Walk":#If they chose to walk or take the bus
        if user_transportation_option == "Take The Bus":#If they chose to take the bus specifically
            print("You go to the bus stop and board the bus, but the bus driver kicks you out because you didn’t pay for a ticket. As you’re broke, you give up and decide to walk.")#Just print this extra piece, no matter what they end up walking
            AdventureGame.universallyhelpfulthings.next_input()#Ensure they're ready to continue

        print("You walk the 3 miles to his house in just under an hour. You sneak behind a bush and try to see if they’re home. You hear someone scream: “Murderer!!!”")

    else:#They chose to follow them using their car
        print("You see that as one of them goes away to put the cart back, they forgot to close the trunk. You could either go inside the trunk and close the door, or you could try to jump on the top just as they leave.")

        #Let them decide whether to enter the trunk or to jump
        user_choice = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Trunk", "Jump"])

        if user_choice == "Trunk":#If they chose to hide in the trunk
            print("You quickly jump inside the trunk and close it shut. You hear the last person enter the car and the car starts. When the car stops, you think you hear the word “nurturer!” being shouted.")

            AdventureGame.universallyhelpfulthings.next_input()#Ensure they're ready to continue

            print("After a few minutes, you think that it’s quiet enough and you get out of the trunk and hide in the bushes. A few seconds later, you hear a scream.")

            AdventureGame.universallyhelpfulthings.next_input()#Ensure they're ready to continue

            bush()#They continue hiding with bush() and can continue from there

        else:#They chose to jump on top of their car
            print("You wait on the side and see the person close the trunk and enter. They are beginning to drive just in front of you, so it’s your time to jump!")

            AdventureGame.universallyhelpfulthings.next_input()#Ensure they're ready to continue to the game

            #Open a mini-game
            jump_game()

def jump_game():
    """This is a simple game that involves the user pressing "enter" in the gap between 2 and 2.5 seconds. It will forward the user elsewhere depending on the outcome."""
    print("Press enter in the gap between 2 and 2.5 seconds to jump on the car! When you want to start, press enter!")

    AdventureGame.universallyhelpfulthings.next_input("Start")#Ensure that they are ready to start the game

    starting_time = datetime.now()#Get the starting time
    input()#Space for them to press enter
    ending_time = datetime.now()#Get the ending time

    time_taken = ending_time - starting_time#Calculate the timedelta

    time_taken = time_taken.total_seconds()#Get the number of seconds with decimals

    if 2 <= time_taken <= 2.5:#If they took from 2 to 2.5 seconds
        #Let them pass through
        print("You safely jumped on the car and WON THE GAME!!!")

        AdventureGame.universallyhelpfulthings.next_input()#Ensure that they are ready to continue
        AdventureGame.universallyhelpfulthings.change_user_score_by(750)#This was a minigame, but a game nonetheless, so give them points

        print("Clutching to the top of the car, you manage to hang on until the end when you jump off just before they turn into their driveway. You hide behind a bush and hear a scary shout: “Murderer!!!”")

        bush()#Push them to bush() to continue the story
    else:#They lost!!
        print("You lose the game and fall off. You decide to follow someone else instead.")

        AdventureGame.universallyhelpfulthings.next_input()  # Ensure that they are ready to continue
        AdventureGame.universallyhelpfulthings.change_user_score_by(-750)  # This was a minigame, but a game nonetheless, so take away some points

        follow_someone_else()  # Push them to follow_someone_else() to continue the story




def follow_someone_else():
    """This is what happens when they choose to follow someone else. It's just a straight line of print statements and next requests until it's forwarded to bush()."""
    pass#PLS FINISH!!!

def bush():
    """This is a central point within this module which just prints out some text and lets the user choose where to go from here."""

    print("Hearing that, you stay hidden for a few more minutes. Eventually, you come out from behind the bushes and look around. Where do you go now?")

    #Let them choose where to go
    user_path = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Stand in front of the house", "The back of the house"])

    if user_path == "Stand in front of the house":#If they chose to stand in front of the house
        print("You stand in front of the house and hear screams from across the street and from within the house you were just hiding beside. Should you return to the bush or leave?")

        #Let them choose where to go now
        user_path_from_front = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Return to the bush", "Leave"])

        if user_path_from_front == "Return to the bush":#If they wanted to return to the bush
            bush()#Call bush once more. A function that calls itself! Recursion!
        else:#They decided to actually leave
            print("Once you get back to your Walmart bathroom stall, you are confronted with another choice, whether to search again or to leave this chaos for a different route?")

            #Let them pick their path from here
            user_path_leaving = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Take a different route", "Search again"])

            if user_path_leaving == "Take a different route":#If they decided to leave this part of the game
                # AdventureGame.restart.main()
                pass
            else:#If they decided to just follow the other person
                #follow_someone_else() - FINISH
                pass
    else:#If they decided to go to the back of the house
        back_of_the_house()#Send them to the back of the house function



def back_of_the_house():
    """This is the real material in this part of the game! It shows the biggest part of the storyline for this section and forwards to different games and storylines."""

    print("You look in the window and see a person dragging a sack labeled “Flour” across the floor. You also see a few more people quietly lied back, watching TV.")
    #CONTINUE!!!!



# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    jump_game()
