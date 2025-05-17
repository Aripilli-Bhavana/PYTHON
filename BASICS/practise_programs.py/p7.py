'''
Write a Python program that:

Takes a string input from the user.

Prints True if the string starts and ends with the same character (case-insensitive).

Otherwise, prints False.'''

x=input("Enter a string: ")
if x[0].lower() == x[-1].lower():
    print(True)
else:
    print(False)