addSet = {1, 2, 3}
addSet.add(4) # Adds an element to the set.
print(addSet) # Output: {1, 2, 3, 4}

removeSet = {1, 2, 3}
removeSet.remove(2) # Removes the element from the set. Raises an error if the element is not found.
print(removeSet) # Output: {1, 3}

discardSet = {1, 2, 3}
discardSet.discard(2) # Removes the element from the set if it is present. Does not raise an error.
print(discardSet) # Output: {1, 3}

popSet = {1, 2, 3}
element = popSet.pop() # Removes and returns an arbitrary element from the set. Error if empty.
print(element) # Output: 1 (or any other element)
print(popSet) # Output: {2, 3} (or the remaining elements)

clearSet = {1, 2, 3}
clearSet.clear() # Removes all elements from the set.
print(clearSet) # Output: set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
unionSet = set1.union(set2) # Returns a new set with elements from the set and all others.
print(unionSet) # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersectionSet = set1.intersection(set2) # Returns a new set with common elements.
print(intersectionSet) # Output: {2, 3}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
differenceSet = set1.difference(set2) # Returns a new set with different elements.
print(differenceSet) # Output: {1}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
symDiffSet = set1.symmetric_difference(set2) # Returns a new set with elements in either or set.
print(symDiffSet) # Output: {1, 4}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2) # Updates the set, adding elements from all others.
print(set1) # Output: {1, 2, 3, 4, 5}