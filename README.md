# MyDict
Custom dictionary-like class realisation.

My own MyDict class that behaves like a dictionary. Support the following operations:

__init__(): Initialize an empty dictionary.
__getitem__(key): Get the value by the key. If the key does not exist, return None.
__setitem__(key, value): Set the value by the key.
__delitem__(key): Delete the item by the key. If the key does not exist, do nothing.
keys(): Return a list of all the keys in the dictionary.
values(): Return a list of all the values ​​in the dictionary.
items(): Return a list of (key, value) pairs in the dictionary.
__str__(): Return a string representation of the dictionary for debugging purposes.

Usage example:

my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name']) # Returns 'Alice'
print('city' in my_dict) # Returns False
del my_dict['age']
print(my_dict.keys()) # Returns ['name']
print(my_dict.values()) # Returns ['Alice']

This class provides similar behavior to Python's built-in dictionaries, but the algorithmic complexity of obtaining an element is O(n) instead of O(1) since MyDict does not use hashing.
