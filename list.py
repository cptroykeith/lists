#list and definite loops
'''
friends = ['roy', 'keith', 'william']
for friend in friends :
    print('Happy new Year:', friend)
print('Done')
'''
#looking inside lists
'''
friends = ['roy', 'keith', 'william']
print(friends[1])
'''
#lists are Mutable/changable
'''
fruit = 'Banana'
fruit[0] = 'b'
x = fruit.lower()
print(x)

lotto = [2, 14, 25, 41, 65]
print(lotto)
lotto[2] = 28

print(lotto)
'''
# using the len and range function
'''
friends = ['roy', 'keith', 'william']
print(len(friends))

print(range(len(friends)))
'''
'''
#adding of list
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
'''
#list slicing
'''
t = [1, 2, 3, 4, 5, 6]
print(t[1:3])
print(t[4:])
print(t[:])
'''
#building a list 
'''
stuff = list()
stuff.append('book')
stuff.append(88)
print(stuff)
stuff.append('cookie')
print(stuff)
'''

#sorting of list
'''
friends = ['roy', 'keith', 'william']
friends.sort()
print(friends)
print(friends[1])
'''
#built-in functions and lists
'''
nums = [2, 14, 25, 41, 65]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
'''
#getting average of a number ,method1
'''
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:',average)

#method2
numlist = list()
while True:
     inp = input('Enter a number: ')
     if inp == 'done' : break
     value = float(inp)
     numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
'''

#split
abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
#you can specify what delimiter character to use in the split
line = 'first;second;third'
thing = line.split(';')
print(thing)
print(len(thing))
