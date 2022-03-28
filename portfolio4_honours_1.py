# Day 1 Conditionals Task 4: Honours Classification
"""
Write a python program that does the following:
1.	Accepts a student’s first name, last name and weighted average mark from the keyboard.
2.	Print an error message if 
a.	the weighted mark is not between 0 and 100
b.	otherwise, determine the student’s average using the following table.
3.	If all the inputs are valid, print first name, last name 
and the appropriate honours classification and congratulatory message.
"""

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
w_average = int(input("What is your weighted average? "))
valid_average = True

if(w_average < 0 or w_average > 100):
    print("Please start again and re-enter a valid weighted average between 0 and 100.")
    valid_average = False
elif(w_average >= 70 and w_average <= 100):
    classification = "First Class"
    message = "Excellent, well done!"
elif(w_average >= 60 and w_average < 70):
    classification = "Upper Second"
    message = "Very good, well done!"
elif(w_average >= 50 and w_average < 60):
    classification = "Lower Second"
    message = "Good, well done!"
elif(w_average >= 40 and w_average < 50):
    classification = "Third Class"
    message = "Could have done better!"
elif(w_average >= 35 and w_average < 40):
    classification = "Pass Degree"
    message = "Work harder next time!"
elif(w_average < 35):
    classification = "Fail"
    message = "Oh dear, try again!"

if(valid_average == True):
    print("Hello", first_name, last_name + ".")
    print("You input", w_average, "for your weighted average.")
    print("Your honours classification is ", classification, ".", " ",  message, sep='')
