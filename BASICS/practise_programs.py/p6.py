'''
Try writing a program that checks:

If the string starts with a vowel (a, e, i, o, u)

And the string ends with a consonant

Print "Valid" if both are true, else print "Not Valid".'''

x=input("Enter a string: ")
if x[0].lower() in "aeiou" and x[-1].lower() not in "aeiou":
    print("Valid")
else:
    print("Not Valid")