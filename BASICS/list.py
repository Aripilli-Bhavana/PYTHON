#list using loops 
'''
fruits = ["aple", "banana", "kiwi"]
for x in fruits:
    print(x)#['aple', 'banana', 'kiwi']

for i in range(len(fruits)):
    print(fruits[i])



fruits = ["aple", "banana", "kiwi"]
i=0
while i < len(fruits):
    print(fruits[i])
    i = i+1 
     #aple
     #banana
     #kiwi

print((x) for x in fruits)

'''
#list comprehension - without 
fruits = ["apple", "banana", "kiwi"]
new = []
for x in fruits:
    if "a" in x:
        new.append(x)
print(new)

#with 
newlist = [x for x in fruits if "a" in x]
print(new)


#copy a list 
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#slicing in lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)