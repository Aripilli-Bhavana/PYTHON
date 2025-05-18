'''Print the length
Write a program to print the length of each word of the sentence given below as well as the length of the whole sentence.
"Coding on CodeChef"

Note: Please print the outputs in the same format as given below.

Output Format
Coding - 6
on - 2
CodeChef - 8
Coding on CodeChef - 18''''''# cook your dish here
s = "Coding on CodeChef"
print("Coding - 6")
print("on - 2")
print("CodeChef - 8")
print("Coding on CodeChef - 18")

'''
'''
s= "Coding on CodeChef"
print(s[0:6], "-", len("Coding"))
print(s[7:9], "-", len("on"))
print(s[10:], "-", len("CodeChef"))

print(s,"-", len(s))
'''
s= "Coding on CodeChef"
words = s.split()
for word in words:
    print(word,"-",len(word))
print(s,"-", len(s))