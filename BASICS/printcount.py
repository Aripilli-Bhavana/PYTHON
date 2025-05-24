#print the number of vowels are present in the string 
n = input()
count  = 0
for char in n:
    if  char in "aeiou":
        count += 1
print(count)