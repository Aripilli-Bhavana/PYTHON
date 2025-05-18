#append

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)#['apple', 'banana', 'cherry', 'orange']
'''
#clear
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits) #[]

'''
#copy - returns a copy of items 
x=fruits.copy()
print(x)

#count - counts the number of elements with specific value
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")#1

#entend 
cars = ["bmw","skoda","audi"]
people = ["a","b","c"]
cars.extend(people)

#index
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")#2

