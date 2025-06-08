'''
AB Difference
Chef is taking his baby steps into the world of programming.

The very first program he's tasked to write is as follows:
"Given two integers 
A
A and 
B
B, print 
A
+
B
A+B."

Unfortunately, Chef makes a typo: his program outputs 
A
×
B
A×B instead of 
A
+
B
A+B.'''

a, b = map(int, input().split())
print(abs((a * b) - (a + b)))
