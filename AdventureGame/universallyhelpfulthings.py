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
# 4/23/2025
#----------
#Version #:
#0.0
#----------
#Interpreter:
#Python 3.11
#----------
#Imports

#----------

def multiple_choice_input_collection(options:list):
    """This function, given a list of options in a list, will order them 1 through n and will let the user enter
    a number to select one of them. The selected answer will be returned back."""

    print("Your options are below:\n")

    #Display options with the numbers by using enumerate
    for number, option in enumerate(options, 1):
        print(f"{number}. {option}")

    print("\nPlease enter the number attached to the option you desire.")

    while True:#Forever loop to force correct entry and prevent non-integer and otherwise improper inputs
        user_input = input().strip()

        try:
            user_input = int(user_input)
            assert user_input <= len(options)
        except ValueError:
            print()

    #CONTINUE!!!!