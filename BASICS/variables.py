'''#multiple values to multiple variables
x, y, z = 50, 60, 80
print(x)
print(y)
print(z)

a, b, c = "add", "sub", "mul"
print(a)
print(b)
print(c)

#one value to multiple varialbes 

j = k = l = "jack"
print(l)



#unpack a collection of items

fruits = ["apple", "mango", "grape"]
x, y, z = fruits
print(x)
print(y)#applemango

#output variables 
x="I"
y="am"
z="Bhavana"
print(x,y,z) #I am Bhavana

x="I"
y="am"
z="Bhavana"
print(x + y + z)#IamBhavana

#for numbers + works as a mathematical operator
x=5
y=10
print(x+y)
'''
m=5
y="Bhav"
print(m+y)#unsupported operator
'''

g='ANA'
F=5
print(g, F)

a='Hello'
b="World"
print(a+b) #HelloWorld print(a,b) #Hello World

'''

x='awesone'
def myfunc():
    print("python is " + x)

myfunc()