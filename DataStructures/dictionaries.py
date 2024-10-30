keysDict = {'a': 1, 'b': 2, 'c': 3}
keys = keysDict.keys() # Returns a list view of all the keys in the dictionary.
print(keys) # Output: dict_keys(['a', 'b', 'c'])

valuesDict = {'a': 1, 'b': 2, 'c': 3}
values = valuesDict.values() # Returns a list view of all the values in the dictionary.
print(values) # Output: dict_values([1, 2, 3])

itemsDict = {'a': 1, 'b': 2, 'c': 3}
items = itemsDict.items() # Returns a list view of dictionary’s key-value tuple pairs.
print(items) # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

getDict = {'a': 1, 'b': 2, 'c': 3}
value = getDict.get('b') # Returns the value for a specified key if the key is in the dictionary.
print(value) # Output: 2

updateDict = {'a': 1, 'b': 2}
updateDict.update({'c': 3, 'd': 4}) # Updates the dictionary with the elements from another dictionary.
print(updateDict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

popDict = {'a': 1, 'b': 2, 'c': 3}
value = popDict.pop('b') # Removes the specified key and returns the corresponding value.
print(value) # Output: 2
print(popDict) # Output: {'a': 1, 'c': 3}

clearDict = {'a': 1, 'b': 2, 'c': 3}
clearDict.clear() # Removes all items from the dictionary.
print(clearDict) # Output: {}

defaultDict = {'a': 1, 'b': 2}
value = defaultDict.setdefault('c', 3) # Returns the value of a key.
print(value) # Output: 3
print(defaultDict) # Output: {'a': 1, 'b': 2, 'c': 3}

copyDict = {'a': 1, 'b': 2, 'c': 3}
new_dict = copyDict.copy() # Returns a copy of the dictionary.
print(new_dict) # Output: {'a': 1, 'b': 2, 'c': 3}

popItemDict = {'a': 1, 'b': 2, 'c': 3}
item = popItemDict.popitem() # Removes and returns the last inserted key-value pair as a tuple.
print(item) # Output: ('c', 3)
print(popItemDict) # Output: {'a': 1, 'b': 2}