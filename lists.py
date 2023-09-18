names = ['john', 'dennis', 'vivian', 'rono', 'amos']
names[0] = 'mike'
names.sort()
names.append('james')
names.insert(0, 'odong')
names.remove('vivian')
names.pop() #removes the last item
print(names.count('rono'))
names2 = names.copy() #takes a copy of the list but does not affect the other.
print(names2)
print('dennis' in names) #checks exitence, returns true or false
#names.clear() #removes all..
print(names) 

numbers = [1,2,3,4,5,6,7,8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)