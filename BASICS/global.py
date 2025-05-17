x='awesone'
def myfunc():
    print("python is " + x)

myfunc()

#gv can be accessed both inside and outside the function 

'''
x='fantastic'
def ymc():
    y="magic"
    print("Python is ",x, y) #Python is  fantastic magic
ymc()
print(x+y)#NameError: name 'y' is not defined
'''

#global variable inside  function 

def dfgh():
    global b
    b='hurray'
    print(b)
dfgh()

print('python is' + b)

