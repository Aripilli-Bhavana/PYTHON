#Write a program to calculate the sum of first N multiples of 3 and print it.

n = int(input())
sum = 0
i =1
for i in range(1,n+1):
    mul = 3*i
    sum =mul+sum
    i += 1
print(sum)
