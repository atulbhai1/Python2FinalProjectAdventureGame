# ----------
# AdventureGame/MurderMysteryPath/askforhelpPiPies.py
# ----------
# Description:
"""This file is the main file for the Murder Mystery pathway which the user can take by choosing to Find an Existing Pie."""

# ----------
# Created:
# 4/29/2025
# ----------
# Last Modified:
# 5/2/2025
# ----------
# Version #:
# 0.2
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings
from datetime import datetime, timedelta
import AdventureGame.theend
import random
import AdventureGame.jail
import AdventureGame.restart

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
        bush()#Continue the story with bush()

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

            #Open a mini-game which will redirect them from there
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

    print("You decide to follow the store manager instead because you overheard him saying that he was going to get a great American Apple Pie.")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they're ready to continue

    print("You manage to sneak into the trunk of his car and wait for the car to stop. As you wait in the back, you notice a few empty sacks labelled “Flour”, some rope, and an unopened box of butcher’s knives.")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they're ready to continue

    print("You feel the car stop and Bob get out. When you think you’re safe, you quickly get out and hide behind a bush. While hiding, you see Bob return to the car and take all the things from the trunk.")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they're ready to continue

    print("Just after he goes inside, you hear some screams from inside and another car pulls in, so you decide to stay hidden.")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they're ready to continue

    print("After a few seconds, you hear someone shout: “Murderer!!!”")

    AdventureGame.universallyhelpfulthings.next_input()  # Make sure that they're ready to continue

    bush()#Send them to bush() to continue the story

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
                AdventureGame.restart.main()#Send them to restart

            else:#If they decided to just follow the other person
                follow_someone_else()#Redirect them to follow_someone_else()

    else:#If they decided to go to the back of the house
        back_of_the_house()#Send them to the back of the house function

def back_of_the_house():
    """This is the real material in this part of the game! It shows the biggest part of the storyline for this section and forwards to different games and storylines."""

    print("You look in the window and see a person dragging a sack labeled “Flour” across the floor. You also see a few more people quietly lied back, watching TV.")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure they're ready to continue

    print("As the person dragging the sack goes into the garage, you see that you have a great chance to rush in, grab the pie, and eat it.")

    #Get the user's choice of path
    user_choice = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Enter", "Return to bush"])

    if user_choice == "Return to bush":#If they chose to go back to the bush
        print("You return to the bush and hear another scream.")

        AdventureGame.universallyhelpfulthings.next_input()  # Make sure they're ready to continue

        bush()#Send them back to the bush
        return None#When it sends them back, you don't want to run the rest of this function, so end this path with return

    #They chose to Enter

    # This is a bad idea, it was made as clear as possible that there is a murderer in this house, so remove a few points.
    AdventureGame.universallyhelpfulthings.change_user_score_by(-400)

    print("As he closes the door behind him, you quietly open the door and see that there are mouse traps all over the floor for some reason. You have to dodge them to cross over to the kitchen where the pie sits on the countertop, nice and fresh.")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they're ready before starting the game!

    mousetraps_game()#Redirect them to the mousetraps_game() function which will play a game and push them forth from there

def mousetraps_game():
    """This is a game where players have to press r and l at least 30 times in 20 seconds. Once they have entered r and l 30 times, the game will automatically end and will check how much time they took. Depending on whether they won, they are redirected accordingly."""

    #Introduce the game
    print("In this game, you have to press r and l in order at least 30 times each within 20 seconds to win and cross the mousetraps. Once you press enter, the game will end and your accuracy and time will be calculated. A single letter not in order means losing.")

    print("Press enter to start")
    input()#Make sure that they are ready to start

    start_time = datetime.now()#Save the start time

    user_gameplay = input("Enter those letters!(Press Enter again to end!")#Let them play and save their response

    end_time = datetime.now()#Save the end time

    user_won = True#By default, the user wins

    taken_time = end_time - start_time#Calculate the timedelta between the starting and ending time
    taken_time = taken_time.seconds#Get the number of seconds that passed from the timedelta

    if taken_time > 20:#If they took over 20 seconds
        user_won = False#They lose!

    user_gameplay = list(user_gameplay)#Make the user gameplay a list for easier review

    if len(user_gameplay) < 60:#If they didn't enter at least 60 letters, they couldn't have done 30 of each!
        user_won = False#So they lost!

    for index, item in enumerate(user_gameplay):#Break user gameplay up as an iterable and for each item and the corresponding index, run the below
        if index % 2 == 0:#If the index is even, so indexes 0, 2, 4, etc... and thus all the "r"'s
            if item != "r":#If they didn't enter the right letter
                user_won = False#They lose!
        else:#If the index is odd, so indexes 1, 3, 5, etc... and thus all the "l"'s
            if item != "l":#If they didn't enter the right letter
                user_won = False#They lose!

    if user_won:#If they won!
        print("\nGREAT JOB! YOU MADE IT!\n")

        AdventureGame.universallyhelpfulthings.change_user_score_by(750)#For having won this small game, give them points!

        AdventureGame.universallyhelpfulthings.next_input()#Make sure that they are ready to continue

        print("You finally get your hands on the pie and are now faced with a great dilemma: whether to eat the pie now or to take it away?")

        #Let them chose to eat it now or take it away
        user_pie_choice = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Take it away", "Eat now"])

        if user_pie_choice == "Take it away":#If they chose to take it away
            take_it_away()
        else:#If they chose to eat it here
            print("You decide to snarf it down right now, but halfway through eating the pie, the door opens and you see a person approaching. You try to run away but get caught up in innumerable mouse traps.")

            AdventureGame.universallyhelpfulthings.next_input()  # Make sure that they are ready to continue

            killer_approaches_but_player_stuck()#Send them to this function to continue
    else:#If they lost

        AdventureGame.universallyhelpfulthings.change_user_score_by(-750)  # For having lost this small game, take away some points!

        print("YOU LOST!!! OH NO!!!")

        AdventureGame.universallyhelpfulthings.next_input()  # Make sure that they are ready to continue

        print("You get a foot trapped in a mousetrap and it hurts horribly. As much as you try to escape, each movement just sets off another trap on another part of your body. The door opens and you see a person approaching.")

        AdventureGame.universallyhelpfulthings.next_input()  # Make sure that they are ready to continue

        killer_approaches_but_player_stuck()  # Send them to this function to continue

def killer_approaches_but_player_stuck():
    """This is a short module used to collect users from 2 paths and consolidate them before the next consolidation at killer_talks_with_minigame()"""

    print("As the person approaches, you notice that their shirt is covered in blood. When they finally reach to tower above your mouse-trap covered body, you recognize who it is…")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they are ready to continue

    print("The store manager from the Walmart!!!")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they are ready to continue

    print("Luckily, it seems like he doesn’t recognize you because of the mouse traps.")

    AdventureGame.universallyhelpfulthings.next_input()#Make sure that they are ready to continue

    killer_talks_with_minigame()#Send them to the killer talking and the related minigame

def take_it_away():
    """This function is what happens when the user chooses to take the pie away. It is a straight line until it diverges with the math quiz game."""

    print("Just after you navigate your way across the sea of mousetraps and open the door to leave again, the person returns from the garage and stares at you for a good 5 seconds.")

    AdventureGame.universallyhelpfulthings.next_input()#Let them continue with a next input

    print("He then immediately starts chasing you and you flee, rushing through other people’s yards and running onto the road.")

    AdventureGame.universallyhelpfulthings.next_input()#Let them continue with a next input

    print("You run down the road and are confronted by a giant wall of numbers, numbers, and numbers!!!")

    AdventureGame.universallyhelpfulthings.next_input()#Let them continue with a next input

    math_game()#Let them continue with the math game

def math_game():
    """This is a simple math game that asks the user to add, subtract, or multiply one-digit numbers. They are forwarded onward based off their results."""

    print("Answer all 10 questions correctly to cross the wall of math. Press enter to start")
    input()#Wait until they are ready to start

    all_correct = True#By default, all responses are correct until the user gets one wrong

    for i in range(10):#For 10 questions
        #Pick 2 numbers from 0 through 9
        num_1 = random.randint(0, 9)
        num_2 = random.randint(0, 9)

        operator = random.choice(["+", "-", "*"])#Randomly pick from addition, subtraction, and multiplication

        equation = f"{num_1}{operator}{num_2}"#Construct the equation

        print(f"Answer the following question:\n{equation}")#Show them the question

        user_response_int = AdventureGame.universallyhelpfulthings.specific_type_input_collection(int)#Get int input

        if eval(equation) != user_response_int:#Evaluate the equation and check if the answer is not the same as the user's response. If so:
            all_correct = False#Not all of the user's answers were right! Shocking!

    if all_correct:#If all of the answers were correct
        print("YOU WIN!!!")
        AdventureGame.universallyhelpfulthings.change_user_score_by(1000)#Give them points for having won

        AdventureGame.universallyhelpfulthings.next_input()#Ensure that they are ready to continue to the next thing

        print("You manage to conquer the numbers and leave the person behind to try and fight against them.")

        AdventureGame.universallyhelpfulthings.change_user_score_by(1000)#Give them points for having gotten a pie!

        AdventureGame.universallyhelpfulthings.next_input()  # Ensure that they are ready to continue to the next thing

        #Send them to the end with the theend module
        AdventureGame.theend.main("You manage to run back to your Walmart bathroom stall and live a happy, contented life from then onwards, knowing that you have a True American Apple Pie in your possession.\nThe End")

    else:#Not all answers were correct!
        print("You lost!")
        AdventureGame.universallyhelpfulthings.change_user_score_by(-1000)#They lost the game and got caught by the killer!

        AdventureGame.universallyhelpfulthings.next_input()#Make sure that they are ready to continue

        print("You lose, overcome by numbers. You watch him approach and recognize him: he’s the manager of that Walmart you live in! Luckily, it seems like he can’t recognize you because of all the numbers piled above you.")

        AdventureGame.universallyhelpfulthings.next_input()  # Make sure that they are ready to continue

        killer_talks_with_minigame()#Send the user to the part with the killer talking to them

def killer_talks_with_minigame():
    """This runs one piece of dialogue, asks the user a question, and redirects them based off their answer to that question."""

    print("He talks to you: “Hello you sly, thief! You’re trying to profit off of my murder!!! How dare you!!! I’ll give you one chance to escape with your life. If you can guess my name, I’ll just frame you for the murder, take my pie, and leave you here. If you can’t though, I won’t think twice before killing you.”")

    user_input = input("Guess his name!").strip().lower()#Ask the user to solve the dillema!

    if user_input == "bob":#If they were right!

        AdventureGame.universallyhelpfulthings.change_user_score_by(300)#At least they kept their lives? So give them a few points

        print("\nA few hours later, police arrive at the scene to see several dead bodies and you lying unconscious with a knife and gun. You plead insanity and are imprisoned. GO TO JAIL!")

        AdventureGame.universallyhelpfulthings.next_input()  # Make sure that they are ready to continue

        AdventureGame.jail.main()#Send them to jail
    else:#If they were wrong

        AdventureGame.universallyhelpfulthings.change_user_score_by(-300)#On top of the death penalty, also penalize them for not being able to guess his name.

        print("\nHe reveals his real name: Bob, and stuffs you inside a sack. You smell a weird combination of blood and flour in the sack that you think must have the same taste as the True American Apple Pie. After letting you lie in the sack for a few minutes while he finishes cleaning up the house, he stabs the sack several times and dumps it into a river. ")

        AdventureGame.universallyhelpfulthings.next_input()  # Make sure that they are ready to continue

        AdventureGame.theend.death()#Send them to death at the end


# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()

#NOTE: There is only one file in this folder because of just how interconnected this path is and how small each of the sections are.