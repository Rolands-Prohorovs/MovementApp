# Import the array module and create an array.
import array
# Create an array of integers
exampleArray = array.array('i', [1, 2, 3, 4])
print(exampleArray) # Output: array('i', [1, 2, 3, 4])

exampleArray.append(5) # Adds an element to the end of the array.
print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5])

exampleArray.extend([6, 7]) # Extends the array by appending elements from another array.
print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

exampleArray.insert(1, 10) # Inserts an element at a given index.
print(exampleArray) # Output: array('i', [1, 10, 2, 3, 4, 5, 6, 7])

exampleArray.remove(10) # Removes the first occurrence of a given value.
print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

element = exampleArray.pop() # Removes and returns the element at the given index or the last element.
print(element) # Output: 7
print(exampleArray) # Output: array('i', [1, 2, 3, 4, 5, 6])

index = exampleArray.index(4) # Returns the index of the first occurrence of a given value.
print(index) # Output: 3

exampleArray.reverse() # Reverses the order of the array.
print(exampleArray) # Output: array('i', [6, 5, 4, 3, 2, 1])
count = exampleArray.count(4) # Returns the number of occurrences of a specified value.
print(count) # Output: 1