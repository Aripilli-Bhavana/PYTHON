#even numbers 
n = int(input("ENTER A NUMBER: "))
i =0
while i <= n:
    print(i)
    i += 2
    if i > n:
        break


for i in range(0,n+1,2):
    print(i)
    