#decreasing triangle pattern

''' 
* * * * * i = 0
* * * *  i =1
* * * i=2
* *i=3
* i=4
'''

print("ENTER:")
n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()



print("Enter")
n= int(input())
for i in range(n):
    for j in range(i,n):
        print("*", end = " ")
    print()





print("Enter")
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end =" ")
    print()