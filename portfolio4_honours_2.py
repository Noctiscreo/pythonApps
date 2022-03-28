# Day 2 Portfolio Question: Honours Classification
"""
1.	You create a function for determining the honours classification.
    The function should accept the weighted average mark and return the honours classification.
2.	Create a function to determine the congratulatory message.
    The function should accept the weighted average mark and return the congratulatory message. 
"""
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
w_average = int(input("What is your weighted average?: "))

# Get weighted average and determine classification:
def get_classification(w_average):
    if(w_average < 0 or w_average > 100):
        print("Please start again and re-enter a valid weighted average between 0 and 100.")
        w_average_new = int(input("What is your weighted average?: "))
        classification = get_classification(w_average_new)
    elif(w_average >= 70 and w_average <= 100):
        classification = "First Class"
    elif(w_average >= 60 and w_average < 70):
        classification = "Upper Second"
    elif(w_average >= 50 and w_average < 60):
        classification = "Lower Second"
    elif(w_average >= 40 and w_average < 50):
        classification = "Third Class"
    elif(w_average >= 35 and w_average < 40):
        classification = "Pass Degree"
    elif(w_average < 35):
        classification = "Fail"

    return classification

classification = get_classification(w_average)

# Determine congratulatory message:
def congratulatory_message(classification):
    if (classification == "First Class"):
        message = "Excellent, well done!"
    elif(classification == "Upper Second"):
        message = "Very good, well done!"
    elif(classification == "Lower Second"):
        message = "Good, well done!"
    elif(classification == "Third Class"):
        message = "Could have done better!"
    elif(classification == "Pass Degree"):
        message = "Work harder next time!"
    elif(classification == "Fail"):
        message = "Oh dear, try again!"

    return message

message = congratulatory_message(classification)

print("Hello", first_name, last_name + ".")
print("Your honours classification is ", classification, ".", " ",  message, sep='')

