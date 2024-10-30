# import Counter and create a counter.
from collections import Counter

# Create a Counter from a list
exampleCounter = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(exampleCounter) # Output: Counter({'b': 3, 'a': 2, 'c': 1})

elements = list(exampleCounter.elements()) # Returns an iterator over elements repeating each as many times as its count.
print(elements) # Output: ['a', 'a', 'b', 'b', 'b', 'c']

common = exampleCounter.most_common(2) # Returns a list of the n most common elements and their counts from the most common to the least.
print(common) # Output: [('b', 3), ('a', 2)]

exampleCounter.subtract(['a', 'b', 'b']) # Subtracts element counts from another iterable or counter.
print(exampleCounter) # Output: Counter({'b': 1, 'a': 1, 'c': 1})

exampleCounter.update(['a', 'b', 'b', 'd']) # Adds counts for elements from another iterable or counter.
print(exampleCounter) # Output: Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

new_counter = exampleCounter.copy() # Returns a shallow copy of the counter.
print(new_counter) # Output: Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

exampleCounter.clear() # Removes all elements from the counter.
print(exampleCounter) # Output: Counter()