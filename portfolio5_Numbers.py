# Day 3 Portfolio Question: Numbers
"""
1.	Create a new file and name it Numbers
2.	Write a python program that keeps numbers in words in a list 
    (in chronological order), i.e. One, Two, Three…, up to Ten.
3.	Ask the user to enter a number. 
4.	Display the corresponding number in words from the list.
    For example, if the user types in ‘1’, display One.
5.	Ask the user to enter a number to be deleted from the list.
6.	Display the new list.
"""
# Numbers list.
words = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

# Get number and display word from list.
numberRetrieve = int(input("Enter a number from 1 to 10: "))
word_index = numberRetrieve
print(words[word_index-1])

# Get number, delete it from list, then display new list.
numberDelete = int(input("Enter a number to be deleted: "))
word_index = numberDelete
del words[word_index-1]
print(words)