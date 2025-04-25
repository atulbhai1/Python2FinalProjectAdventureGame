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
# 4/24/2025
#----------
#Version #:
#0.1
#----------
#Interpreter:
#Python 3.11
#----------
#Imports

#----------

#The below custom exception is to ensure that the input collection functions can identify when the problem is just an improper input and not another type of problem.
class ImproperInputException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

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
            print(e)
            continue#Loop again
        else:
            break#Stop looping inputs. VALID INPUT!!!

    #Now we have a valid number for input. Convert it and return the result.
    result = options[user_input-1]

    return result

def next_input():
    """This is a simple function that helps us clarify and recognize all the times the user has to press enter to continue reading in code outside of this."""
    print("Enter to continue")
    input()
