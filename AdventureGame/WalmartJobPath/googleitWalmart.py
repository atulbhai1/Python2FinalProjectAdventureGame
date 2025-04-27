# ----------
# AdventureGame/WalmartJobPath/googleitWalmart.py
# ----------
# Description:
"""This file is the main file for the Walmart pathway which the user can take by choosing to Google It."""
# ----------
# Created:
# 4/24/2025
# ----------
# Last Modified:
# 4/26/2025
# ----------
# Version #:
# 0.2
# ----------
# Interpreter:
# Python 3.11
# ----------
# Imports
import AdventureGame.universallyhelpfulthings


def main():
    """This function gives the user the start of a part of a story with choices and different paths. It is the Walmart part of the game.
    It features a game in a different file and also diverges paths further into different files."""

    #Text introduction to this part of the story
    print("You Google how to make a True American Apple Pie and it tells you to gather some ingredients and bake it in an oven. Luckily, you live in a Walmart bathroom, and can just walk over to the baking items section to find the ingredients. But when you walk over, you see that the items you need cost money that you really don’t have(Kinda obvious given where you live). So you need to get a job! You find the perfect place, 30 feet away at a Walmart checkout counter and begin to work. You ask the person from the stall to the right of yours to help you figure out what to do.")

    AdventureGame.universallyhelpfulthings.next_input("Talk to him")#Basically a continue/next prompt

    print("“Hello lad! I see you’re trying to leave me all alone in this Walmart bathroom!”")

    #User Choice, a quick split in the path that quickly merges back

    #These are the 2 possible paths
    path_options = ["“No! No! I just wanted some pie!”", "“Not like that, I just want to be able to upgrade to the Whole Foods Bathrooms, I heard they’re nicer.”"]

    #This following line asks the user what path they want and if they want the first path, it prints out the result.
    if AdventureGame.universallyhelpfulthings.multiple_choice_input_collection(
            path_options) == "“No! No! I just wanted some pie!”":
        print("“Oh, ok! I have one tip for ya, never trust people named Bob, those are horrible, horrible people who will lie, steal, pilfer, and do everything in their power to ruin this world!”")
        AdventureGame.universallyhelpfulthings.change_user_score_by(100)  # Reward the user for appeasing the other person and learning valuable information.
    else:  # If they picked the other path, it prints out a different thing.
        print("“But that’s still trying to leave me! You brat! I refuse to help you!”")
        AdventureGame.universallyhelpfulthings.change_user_score_by(-100)  # Punish the user for having angered the person and losing valuable information.

    #The paths merge again. Give a "Next" prompt(Which is the default for the called function!)
    AdventureGame.universallyhelpfulthings.next_input()

    print("On your first(and last) day on the job, your manager meets you to tell you what you have to do.")

    AdventureGame.universallyhelpfulthings.next_input()#Next prompt

    #This introduces the game to be played!!!
    print("“Hello young chap. I’m Bob, your manager. All you need to do today is ensure that nobody leaves the store with stolen items. You get to stand at the door and check receipts as people leave. I will also be sending people who rob and don’t rob our store. If you fail to capture any robber or capture anyone who’s innocent, I’m not giving you your pay at the end of the day. HAHAHAHAHAHAHAHAHAHA!!!!”")

    #Before the game starts, have a "Start Working" prompt to confirm that they want to start the game!
    AdventureGame.universallyhelpfulthings.next_input("Start Working")

    #Redirect to the game file for this game


# For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main(0)
