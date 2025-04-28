#----------
#AdventureGame/universallyhelpfulthings.py
#----------
#Description:
"""This file contains several essential and universally helpful things like input regulation."""
#----------
#Created:
# 4/23/2025
#----------
#Last Modified:
# 4/27/2025
#----------
#Version #:
#0.3
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import os#For accessing files when unsure of file using this module and of the OS this will be run on


#----------
user_score_file_name = "user_score.txt"

#The reason for the weird avoidance of file paths to be seen is that I am using a Mac to code this and will do my tests on a Mac but also need this to work on a Windows computer

#The below custom exception is to ensure that the input collection functions can identify when the problem is just an improper input and not another type of problem.
class ImproperInputException(BaseException):
    def __init__(self, message):
        self.__message = message#self.__message means that message is a "hidden" object attribute, another thing that might be a requirement
        super().__init__(self.__message)

    def get_message(self):
        """This method just returns the value of the hidden object attribute of self.__message."""
        return self.__message


#Note: The above custom exception makes it so that I have both used Exceptions and Classes! YES!!!!!!

def multiple_choice_input_collection(options:list):
    """This function, given a list of options in a list, will order them 1 through n and will let the user enter
    a number to select one of them. The selected answer will be returned back."""

    print("Your options are below:\n")

    #Display options with the attached numbers by using enumerate
    for number, option in enumerate(options, 1):
        print(f"{number}. {option}")

    print("\nPlease enter the number attached to the option you desire.")

    while True:#Forever loop to force correct entry and prevent non-integer and otherwise improper inputs.
        user_input = input().strip()

        try:
            user_input = int(user_input)
            if user_input > len(options) or user_input < 1:#Must enter a number between 1 and the total number of options.
                #If condiction not met, make a custom error message and raise the custom error
                raise ImproperInputException("Please enter a number between 1 and {0}".format(len(options)))
        except ValueError:#If the number was not an integer
            print("Please enter an integer value for your answer choice.")
            continue#Loop again
        except ImproperInputException as e:#If the number was too high/low, print the error message
            print(e.get_message())#Use the method to get the error message
            continue#Loop again
        else:
            break#Stop looping inputs. VALID INPUT!!!

    #Now we have a valid number for input. Convert it and return the result.
    result = options[user_input-1]

    return result

def next_input(prompt="Next"):
    """This is a simple function that helps us clarify and recognize all the times the user has to press enter to continue reading in code outside of this."""
    print(f"{prompt}(Press enter/return to continue)")
    input()

def user_score_retrieval():
    """This function opens the user_score.txt file, gets the contents, closes the file, and returns the contents as an integer."""
    # If the current directory isn't AdventureGame, move it back to the parent directory which should be AdventureGame
    if str(os.getcwd())[-len("AdventureGame"):] != "AdventureGame":
        os.chdir("..")

    with open(user_score_file_name, "r") as user_score_file:
        user_score = int(user_score_file.read())
        user_score_file.close()

    return user_score

def user_score_redefinition(new_score=0):
    """This function opens user_score.txt, replaces what's indside, and closes it."""

    # If the current directory isn't AdventureGame, move it back to the parent directory which should be AdventureGame
    if str(os.getcwd())[-len("AdventureGame"):] != "AdventureGame":
        os.chdir("..")
    with open(user_score_file_name, "w") as user_score_file:
        user_score_file.write(str(new_score))
        user_score_file.close()

    return True

def change_user_score_by(number):
    """This file gets the user's score, changes it, and saves it back to the file."""
    user_score = user_score_retrieval()
    user_score += number
    user_score_redefinition(user_score)