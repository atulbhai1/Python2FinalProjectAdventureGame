#----------
#AdventureGame/jail.py
#----------
#Description:
"""This file is a central meeting point for the whole project. There are several pathways that end up in jail, making this rather important. It also has a game in case one wants to escape jail!"""
#----------
#Created:
# 4/28/2025
#----------
#Last Modified:
# 5/14/2025
#----------
#Version #:
#0.3
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.universallyhelpfulthings
import AdventureGame.theend
from datetime import datetime, timedelta
import AdventureGame.restart
import time
#----------

def main():
    """This function just reduces the player's score, tells them that they're in jail, and lets them either wait it out or play a game to escape(Forwards to other func.).
    If they survive and leave jail, they are sent to AdventureGame.restart.main()"""

    AdventureGame.universallyhelpfulthings.change_user_score_by(-1000)#Jail is bad, so remove a lot of points!

    print("You're in JAIL!!!! What now?")

    user_choice = AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(["Escape!!!", "Wait out your sentence"])#Get the user's choice

    if user_choice == "Wait out your sentence":#If they wanted to wait it out
        print("You decide to wait out the entirety of your prison sentence, an unbelievably long 30 seconds.")
        print("Waiting...")
        time.sleep(30)#Wait 30 seconds
        print("\nNow that you have waited for the entirety of your unimaginably long prison sentence, you are a free man once more!")
        AdventureGame.restart.main()
    else:
        escape()#Run the escape game!


def escape():
    """This function is a game that relies on the user pressing enter exactly 30 times and then entering n and enter to finish the game.
    If they win, they can leave jail. If they don't win, they die and are sent to AdventureGame.theend.death()"""

    #Inform the user about the game and how to play
    print("\nYou have decided to escape. Thus, you examine at the guard patterns and see where you have to go and when you have to go in order to escape. You even calculate how many footsteps it takes to escape when they take you outdoors: 30. But on the day you plan on escaping, they tighten security due to a terrorist attack and put blindfolds on you! Now you have to walk exactly 30 steps in the 30 seconds you have between guard changes in order to escape! If you’re off by even 1 step, you won’t be able to find the door in time and will get caught!")

    print("\nIn order to play this game, you need to press enter exactly 30 times and enter an input of \"n\" and enter that in order to confirm that you are done. Do all of this within 30 seconds to escape.")

    input("\nRead over the above instructions carefully. When you are ready, press enter to start")#Give them time to read before starting the game

    start_time = datetime.now()#Save the start time

    user_entry = ""#By default, just have an empty string for user entry
    user_entries_list = []#Save all the user entries here to count them

    while user_entry != "n":#While the user hasn't nudged into the door yet
        user_entry = input()#Get user input

        user_entry = user_entry.lower().strip()#Clean user input for checking for the "n"

        if user_entry != "n":#If they didn't enter the ending code
            user_entries_list.append(user_entry)#Save their entry for counting

    #Now the user has finished playing
    end_time = datetime.now()

    user_survives = True

    #First ensure that the user entered 30 times exactly
    if len(user_entries_list) == 30:
        time_difference = end_time - start_time#Then calculate how many seconds they took

        if time_difference.seconds <= 30:#If they took 30 seconds or less
            print("You escaped!!!")#They escaped!
            AdventureGame.restart.main()#Make them restart
            return None#Keep them from going onwards to death
    #If they lost
    print("You stop a bit too late or with not enough or too many steps. Regardless, they shoot you dead then and there.")
    AdventureGame.theend.death()#Do the death sequence




#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
