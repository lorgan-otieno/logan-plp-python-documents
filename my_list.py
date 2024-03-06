#creation of an empty list
my_list =[]

#appending elements to the empty list
my_list.extend([10,20,30,40])

#insertion of 15 at position 2 in the appended list
my_list.insert(1, 15)

#extending my list to 70
my_list.extend([50,60,70])


#removing the last element from the my_list
my_list.pop()
print(my_list)

#sorting my_list in ascending order
my_list.sort()

#finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print("Index of value 30 in my_list:", index_of_30)
print("Updated my_list:", my_list)