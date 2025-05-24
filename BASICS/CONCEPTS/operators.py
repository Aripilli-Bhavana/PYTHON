#arithmetic +,-,*,/,%,**,//
#+
x = 5
y = 3

print(x + y)#8
#/
x = 12.5

y = 3

print(x / y)#4.1667


#% - remainder 
x = 5
y = 2

print(x % y)#1

#**
x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2 #32

#//
x = 15
y = 2

print(x // y)

#the floor division // rounds the result down to the nearest whole number


#assignment operators
#x&=3
x = 5

x &= 3

print(x) #bitwise and 5- 0101 3-0011 #answer is 0001 

x = 5

x |= 3

print(x)# or operator, answer is 0111 - 7

#XOR operation answer is 6
x = 5

x ^= 3

print(x)


#>>= right shift operation , shifts bits to the right
x = 5

x >>= 3

print(x) #0
'''
Original (5):   0101   → 5
After 1 shift:  0010   → 2
After 2 shifts: 0001   → 1
After 3 shifts: 0000   → 0
'''

#<<= left shift operation,  shifts bits to the left
x = 5

x <<= 3

print(x) #40 


#x=3, print(3)
print(x := 3)


#comparison ops ==,!=, >,<,<=,>=


#logical operators - and , or, not
#not
x = 5

print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

#and
x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10


#or
x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)



#identity ops 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y


#bitwise - &,|, ^, ~,<<,>>
#<< - left shift ops - It multiplies the number by 2 for each shift

'''
3 << 2
= 3 × 2 × 2
= 3 × 4
= 12

'''

