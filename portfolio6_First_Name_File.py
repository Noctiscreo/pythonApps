# Day 3 Portfolio Question: First names file
""" 
1.	Create a new file and name it Firstname_File
2.	Using python codes, 
(a) create a text file and name it firstName.txt
(b) write ten different first names to firstName.txt
(c) read contents from firstName.txt
 """

first_names = open("firstName.txt", "x")

first_names.write("John")
first_names.write("\nBob")
first_names.write("\nJack")
first_names.write("\nSally")
first_names.write("\nSarah")
first_names.write("\nPaul")
first_names.write("\nJill")
first_names.write("\nLucy")
first_names.write("\nMary")
first_names.write("\nAngus")
first_names.close()

first_names = open("firstName.txt", "r")
print(first_names.read())
first_names.close()