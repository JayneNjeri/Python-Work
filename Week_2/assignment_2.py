#Creating an empty listt
my_list=[]
print(type(my_list))

#Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Inserting 15 at the second position
my_list.insert(1,15)
print(my_list)

#Extending the list
my_list.extend([50,60,70])
print(my_list)

#Removing the last element from the list
my_list.pop()
print(my_list)

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list.
print(my_list.index(30))

