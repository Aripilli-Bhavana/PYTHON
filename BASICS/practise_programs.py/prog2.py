# Ask the user to enter their full name.
# Then, print:
# 1. The full name
# 2. The first character
# 3. The last character
# 4. The length of the name
# 5. The name in uppercase
name=input("Enter your full name: ")
print("Full name:", name)
print("First Character: ",name[0])
print("Last Character: ", name[-1])
print("Length of the name: ", len(name))
print("Uppercase: ",name.upper())