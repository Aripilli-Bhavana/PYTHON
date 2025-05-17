'''
Write a program that:

Takes a name as input.

Prints:

The first 5 characters

The last 3 characters

The name reversed

Only characters at even indices
'''

name=input("Enter your name: ")

print("The first 5 characters are: ",name[:5])
print("The last 3 characters are: ", name[-3:])
print("The name reversed", name[::-1])
print("Only characters at even indices are: ",name[::2])
