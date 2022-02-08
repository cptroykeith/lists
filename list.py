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
stuff = list()
stuff.append('book')
stuff.append(88)
print(stuff)
stuff.append('cookie')
print(stuff)

