'''
name = "Alice"
age = 25
greeting = f"My name is {name} and I am {age} years old."
print(greeting)
#My name is Alice and I am 25 years old.

name = "Bob"
age = 30
print(f"{name} is {age} years old.")
#Bob is 30 years old.

width = 10
height = 5
print(f"Area of rectangle: {width * height}")
#Area of rectangle: 50

price = 456.765434
print(f"Price is {price:.2f}")#2 decimal places 


for i in range(1, 6):
    print(f"Number: {i:>3}")  # right aligned with width 3
   
Number:   1
Number:   2
Number:   3
Number:   4
Number:   5 
#Create variables first_name and last_name. Use an f-string to print a greeting like:
"Hello, John Doe!" if first_name = "John" and last_name = "Doe".
first_name = "Aripilli"
last_name = "Bhavana"
print(f"Hello, {first_name} {last_name} !") '''
#Format the number pi = 3.14159265359 to print with only 3 decimal places inside a sentence.
pi=3.141592653
print(f"Pi is {pi:.2f}")
#Given two numbers a = 7 and b = 3, print their sum, difference, product, and quotient using one f-string each
a=7
b=3
print(f"Sum is: {a+b}, Diff is: {a-b}")

#Print a table of squares for numbers 1 to 5, aligning the numbers and their squares using f-string formatting.

print(f"{'Number':<10} {"Square":<10}")
for i  in range(1,6):
    print(f"{i:<10} {i**2:<10}")

txt = f"The price is {20 * 59} dollars"
print(txt)
