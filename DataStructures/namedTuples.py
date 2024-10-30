# import namedtuple from the collections module and create a named tuple.
from collections import namedtuple

# Define a named tuple called 'Point'
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of Point
p = Point(1, 2)
print(p) # Output: Point(x=1, y=2)

# You can access the fields of a named tuple by name.
print(p.x) # Output: 1
print(p.y) # Output: 2

# _replace() returns a new named tuple with specified fields replaced with new values.
p2 = p._replace(x=10)
print(p2) # Output: Point(x=10, y=2)

# _asdict() returns the named tuple as an OrderedDict.
p_dict = p._asdict()
print(p_dict) # Output: {'x': 1, 'y': 2}

# _fields returns a tuple of field names of the named tuple.
fields = p._fields
print(fields) # Output: ('x', 'y')

# _make() creates a new instance of the named tuple from an iterable.
p3 = Point._make([3, 4])
print(p3) # Output: Point(x=3, y=4)