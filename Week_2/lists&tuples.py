#Lists[]used to store multiple data at once
#A collection which is ordered and changeable. Allows duplicate members.
#They are mutable meaning one can modify the elements in a list
my_list = [1, 2, 3, 4, 5]
print(my_list)
#Accessing elements in a list using Indexes
print(my_list[0])
#Using the slicing operator : to access a range of elements
#my_list[1:3] returns a list with items from index 1 to index 2.
print(my_list[1:3])
print(my_list[:])
print(my_list[1:])
#using append() to add an element to the end of a list
my_list.append(6)
print(my_list)

for i in my_list:
    print(i)
#Tuples() used to store multiple data at once
#A collection which is ordered and unchangeable. Allows duplicate members.
#They are immutable meaning one cannot modify the elements in a tuple
my_numbers = (1, 2, 3, 4, 5)
#indexing and slicing can be used to access elements in a tuple
# the -1 index is used to access the last element in a tuple
print(my_numbers[-1])



  