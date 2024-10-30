appendList = [1, 2, 3]
appendList.append(4) # Adds an item to the end of the list.
print(appendList) # Output: [1, 2, 3, 4]

extendList = [1, 2, 3]
extendList.extend([4, 5]) # Extends the list by appending elements from another list.
print(extendList) # Output: [1, 2, 3, 4, 5]

insertList = [1, 2, 3]
insertList.insert(1, 'a') # Inserts an item at a specified position.
print(insertList) # Output: [1, 'a', 2, 3]

removeList = [1, 2, 3, 2]
removeList.remove(2) # Removes the first occurrence of a specified value.
print(removeList) # Output: [1, 3, 2]

popList = [1, 2, 3]
item = popList.pop() # Removes and returns the item at the given position or the last item.
print(item) # Output: 3
print(popList) # Output: [1, 2]

clearList = [1, 2, 3]
clearList.clear() # Removes all items from the list.
print(clearList) # Output: []

indexList = [1, 2, 3]
index = indexList.index(2) # Returns the index of the first occurrence of a specified value.
print(index) # Output: 1

countList = [1, 2, 2, 3]
count = countList.count(2) # Returns the number of occurrences of a specified value.
print(count) # Output: 2

sortList = [3, 1, 2]
sortList.sort() # Sorts the list in ascending order.
print(sortList) # Output: [1, 2, 3]

reverseList = [1, 2, 3]
reverseList.reverse() # Reverses the order of the list.
print(reverseList) # Output: [3, 2, 1]

copyList = [1, 2, 3]
newList = copyList.copy() # Returns a shallow copy of the list.
print(newList) # Output: [1, 2, 3]