# Day 1 Portfolio Question: Calculate Age from Year of Birth
""" 
1.	Create a new file and name it Age_From_YoB 
2.	Accept a user’s year of birth from the keyboard 
3.	Calculate the user’s age and print it on the screen 
"""

yearOfBirth = int(input("What year were you born? "))
from datetime import date
todays_date = date.today()

print("You are", (todays_date.year - yearOfBirth), "years old.")
