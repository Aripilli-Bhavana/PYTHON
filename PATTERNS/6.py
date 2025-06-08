#right sided triangle 
'''
         *
       * *
     * * *    
   * * * *  
 * * * * *
  '''
#we need three loops, i for rows, the first j for printing the space, and the second j for printing the stars
print("Enter:")
n= int(input())
for i in range(n):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    print()


print("Enter:")
n= int(input())
for i in range(n):
    for j in range(n-i):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    print()