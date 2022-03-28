# Day 1 Conditionals Portfolio Question: Student gets 10% discount.
"""
1.	A coffee shop offers students 10% discounts on things they buy. Write a program that accepts user input for the cost of an item (e.g. 10.00) and the status of the user (“student” or “staff”). The program must follow the following requirements.
a.	If the user is a staff member, the user will be charged the full amount
b.	Otherwise, if the user is a student, the user gets 10% off the price
c.	Otherwise, if the user status is not “student” or “staff” the user is charged the full amount
2.	Display the amount to be paid on the screen
3.	If the user’s status is NOT “student” or “staff”, display the user is unknown and does not qualify for any discount.
"""

user_unknown = True
student_discount = .10

statusInput = str(input("Student or staff? "))
cost = float(input("What is the cost of the item? "))
status = statusInput.lower()

if(status == 'student'):
    total = cost - (student_discount * cost)
    user_unknown = False
elif(status =='staff'):
    total = cost
    user_unknown = False
else:
    total = cost
    print("User " + status + " is unknown. You do not qualify for a discount.")
    print("Your total cost is: £", format(total, ",.2f"), sep='')

if(user_unknown == False and status == "student"):
    print("You are a student, and so your discount is 10%.")
    print("Your total cost is: £", format(total, ",.2f"), sep='')
elif(user_unknown == False and status == "staff"):
    print("You are staff, and so you don't receive a discount.")
    print("Your total cost is: £", format(total, ",.2f"), sep='')
