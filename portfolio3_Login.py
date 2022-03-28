# Day 2 Portfolio Question: Login System
""" 
1.	Create a new file and name it Login
2.	Write a python program that asks a user for a username and password. 
3.	If the username is not “admin” and password is not “pwd”, the user should be informed that the credentials are wrong and must be given the opportunity to enter them again. 
4.	This must continue until the right credentials have been entered by the user. 
5.	When the correct credentials have been entered, the program should inform the user that the correct credentials have been entered.
"""

valid = False

while(valid == False):
    userName = str(input("Please enter your username: "))
    userPass = str(input("Please enter your password: "))
    if(userName != "admin" or userPass != "pwd"):
        print("Username / password not correct. Please try again.")
    else:
        print("Username and password accepted.")
        valid = True
