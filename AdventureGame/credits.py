#----------
#AdventureGame/credits.py
#----------
#Description:
"""This file displays the credits and dev. info."""
#----------
#Created:
# 4/25/2025
#----------
#Last Modified:
# 4/25/2025
#----------
#Version #:
#0.0
#----------
#Interpreter:
#Python 3.11
#----------
#Imports
import AdventureGame.universallyhelpfulthings
#----------


def main():
    """This function just displays the credits and some of the development info. It uses an f-string with extra
    formatting/styling to center words in the credits section"""

    print("""
{0:-^43}
{1:^43}
{2:^43}
{3:-^43}
""".format("Credits", "Designed and Developed by: Atul Nitin",
           "Project Requirements Provided By: Mr. Dolce", ""))

    print("""
This was developed as Atul's Python 2 CDM Submission. 
This has an overall game map viewable at:
https://docs.google.com/drawings/d/e/2PACX-1vRLgXLf1vPdFrrAytmkgkNtdYS9JGo-kDQ3t5tjBvFgqIKL3-YGDYNtm8rJBYMQhAPNYc0GtbnF4QVC/pub?w=1442&h=1422
Now for real development info!
This game is contained as a Package. An extra file is used in the submitted version of this in order to open and run the package.
This was built on just Python 3.11 using only inbuilt modules and the custom modules defined within this. I am unsure of its backwards compatibility with earlier versions of Python 3. But I can verify that it works on Python 3.11 .
This project was saved on Github for safety as is normal practice. The link to it is https://github.com/atulbhai1/Python2FinalProjectAdventureGame .
Hope you had/will have a great time testing out and playing this game!""")



#For testing purposes, if this file is being run on its own, automatically run main()
if __name__ == "__main__":
    main()
