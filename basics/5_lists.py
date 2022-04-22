#any data type can be put into lists
#it can be mixed
#each element in the list have index




friends = ['hello', 'boys','readdy','boys']

friends[2] # reddy
friends[-2] # boys
friends[1:3] #till 2nd index


#Lists Functions
numbers = [1,2,3,4,5,6]
friends.append('newFriends') #will add new element in the last
print(friends)
friends.extend(numbers) # it will put whole list in the list
friends.insert(1,'hello frend') # will push one element at index 1

friends.remove('hello')


print(friends.index("boys"))
print(friends.count("boys"))  #2

friends.sort() # will sort lexicographically
print(friends) # first numbers will be there then string will be
friends.reverse()

friends2=friends.copy()