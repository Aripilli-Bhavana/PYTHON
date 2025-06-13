#diamond pattern 
''' 
    *   
  * * *
* * * * * 
  * * * 
    *
'''



print("enter")
n= int(input())
for i in range(n):
    print(" " * (n-i-1) + "*" * (i + 1))
for i in range(n-2, -1, -1): 
      print(" " * (n - i -1) + "*" * (i+1))
  


print("Enter")
n= int(input())
for i in range(n):
    for j in range(i,n):
        print("*", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    for j in range(i):
        print("*", end = " ")
    for j in range(i):
        print(" ", end = " ")
    for j in range(i,n):
        print("*", end = " ")
    for j in range(i, n-1):
        print("*", end = " ")
    print()