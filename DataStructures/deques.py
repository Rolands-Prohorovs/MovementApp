# import the deque class and create a deque.
from collections import deque

exampleDeque = deque([1, 2, 3, 4])
print(exampleDeque) # Output: deque([1, 2, 3, 4])

exampleDeque.append(5) # Adds an element to the right end of the deque.
print(exampleDeque) # Output: deque([1, 2, 3, 4, 5])

exampleDeque.appendleft(0) # Adds an element to the left end of the deque.
print(exampleDeque) # Output: deque([0, 1, 2, 3, 4, 5])

element = exampleDeque.pop() # Removes and returns an element from the right end.
print(element) # Output: 5
print(exampleDeque) # Output: deque([0, 1, 2, 3, 4])

element = exampleDeque.popleft() # Removes and returns an element from the left.
print(element) # Output: 0
print(exampleDeque) # Output: deque([1, 2, 3, 4])

exampleDeque.extend([5, 6]) # Extends the right end of the deque.
print(exampleDeque) # Output: deque([1, 2, 3, 4, 5, 6])

exampleDeque.extendleft([0, -1]) # Extends the left end of the deque in reverse order.
print(exampleDeque) # Output: deque([-1, 0, 1, 2, 3, 4, 5, 6])

exampleDeque.rotate(2) # Rotates the deque n steps to the right (or left if negative).
print(exampleDeque) # Output: deque([5, 6, -1, 0, 1, 2, 3, 4])

exampleDeque.rotate(-2)
print(exampleDeque) # Output: deque([-1, 0, 1, 2, 3, 4, 5, 6])

exampleDeque.clear() # Removes all elements from the deque.
print(exampleDeque) # Output: deque([])

exampleDeque = deque([1, 2, 2, 3, 4]) # Counts the number of occurrences of given value.
count = exampleDeque.count(2)
print(count) # Output: 2