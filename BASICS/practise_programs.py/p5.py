'''
Write a Python program to:

Take a string input from the user

Check if the string starts with "Py"

Check if the string ends with "on"

Print True if both conditions are met, otherwise False'''

x=(input("Enter a string: "))
if x[:2] == "Py" and x[-2:] == "on":
    print(True)
else:
    print(False)
