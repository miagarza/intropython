lists_of_numbers= [0,4,5,9,7,8,1,2,6,3]
print(lists_of_numbers)

#append=add, in this case it automatically adds it to the end of the list
lists_of_numbers.append(7)
print(lists_of_numbers)

#adding elements
#first number is always where the number is being inserted in the list, second number is what is being inserted
lists_of_numbers.insert(0,10)
print(lists_of_numbers)

#pop() method removes a element from an index
#to remove a certain element, use remove()

#pop elements
lists_of_numbers.pop()
print(lists_of_numbers)

lists_of_numbers.pop(2)
print(lists_of_numbers)

# remove(element) removes a certain NUMBER

lists_of_numbers.remove(9)
print(lists_of_numbers)

lists_of_numbers.sort()
print(lists_of_numbers)

#now sort strings
list_of_colors = ["yellow", "blue", "purple", "red", "green", "orange"]
list_of_colors.sort()
print(list_of_colors)