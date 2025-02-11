class MyDict(dict):
    def __init__(self):
        super().__init__()
        self.dict_keys = []
        self.dict_vals = []

    def __getitem__(self, key):
        try:
            return self.dict_vals[self.dict_keys.index(key)]
        except ValueError:
            return None
        # Get value by key. If key does not exist, return None.

    def __setitem__(self, key, value):
        if key not in self.dict_keys:
            self.dict_keys.append(key)
            self.dict_vals.append(value)
        else:
            self.dict_vals[self.dict_keys.index(key)] = value
        # Setting a value by key.

    def __delitem__(self, key):
        if key in self.dict_keys:
            index = self.dict_keys.index(key)
            self.dict_vals.pop(index)
            self.dict_keys.pop(index)
        # Delete an element by key. If the key does not exist, do nothing.

    def keys(self):
        return self.dict_keys
        # Return a list of all keys in the dictionary.

    def values(self):
        return self.dict_vals
        # Return a list of all values in the dictionary.

    def items(self):
        return list(zip(self.dict_keys, self.dict_vals))
        # Return a list of (key, value) pairs in a dictionary.

    def __str__(self):
        return_string = ""
        for i in range(len(self.dict_keys)):
            return_string += str(self.dict_keys[i]) + ": " + str(self.dict_vals[i]) + ", "
        return "{" + return_string[:-2] + "}"
        # Return a string representation of the dictionary for debugging purposes.


my_dict = MyDict()
print(my_dict)
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Return 'Alice'
print('city' in my_dict)  # Return False
print(my_dict)
del my_dict['age']
print(my_dict.keys())  # Return ['name']
print(my_dict.values())  # Return ['Alice']
