thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)#allows duplicates


'''
('apple', 'banana', 'cherry')
(1, 5, 7, 9, 3)
(True, False, False)
('apple', 'banana', 'cherry', 1, 5, 7, 9, 3, True, False, False)
'''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
t = tuple1 + tuple2 + tuple3
print(t)


#tuple constructor 

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#range 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

if "apple" in thistuple:
    print("YES")

    #remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#del - keyword - removes the tuple entirely

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


#packing a tuple 
fruits = ("apple", "banana", "cherry")


#unpacking a tuple 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#using asterick *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


