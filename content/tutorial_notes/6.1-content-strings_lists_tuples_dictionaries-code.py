#%% Strings, lists, tuples, and dictionaries
eg_string = "Hello, World!"
eg_list = [1, 3.4, "this is a list", True, False, True]
eg_tuple = (1, 3.4, "this is a tuple", True)

#%% Length (len) function
print(len(eg_string))    # 16, since there are 16 characters
print(len(eg_list))      # 6, since there are 6 objects
print(len(eg_tuple))     # 4, since there are 4 objects

#%% Indexing
eg_string = "Hello, World!"
print(eg_string[0])     # character at index 0, 'H'
print(eg_string[4])     # character at index 4, 'o'
print(eg_string[-1])    # character at index -1, '!'

#%% Slicing
print(eg_string[0:3])       # characters between index 0 and 3, "Hel"
print(eg_string[:6])        # characters until index 6, "Hello,"
print(eg_string[-6:])       # characters from index -6, "World!"
print(eg_string[-10:10])    # "lo, Wor"
print(eg_string[::-1])      # "!dlroW ,olleH"

#%% Indexing and slicing lists and tuples
eg_list = [1, 3.4, "this is a list", True, False, True]
eg_tuple = (1, 3.4, "this is a tuple", True)
print(eg_list[-4])          # "this is a list"
print(eg_list[3:5])         # [True, False]
print(eg_tuple[::-1])       # (True, "this is a tuple", 3.4, 1)

#%% Modifying lists
number_list = [1, 3, 5, 5, 9]
print(number_list)              # [1, 3, 5, 5, 9]
number_list[3] = 7              # modify value at index 3
print(number_list)              # [1, 3, 5, 7, 9]
number_list[0:3] = (0, 2, 4)    # modify values at indices 0, 1, 2
print(number_list)              # [0, 2, 4, 7, 9]

#%% Modifying lists
eg_string = "Hello, World!"
# eg_string[0] = "h"            # causes an error
eg_tuple = (1, 3.4, "this is a tuple", True)
# eg_tuple[0] = 1.1             # causes an error

#%% Modifying lists
new_string = "h" + eg_string[1:]
print(new_string)

# Single element tuples have a comma!
new_tuple = (1.1, ) + eg_tuple[1:]
print(new_tuple)

#%% Arithmetic operators
print("a" * 2 + "bc" + "123")       # aabc123
print(["a", "b"] * 2 + [2, 3])      # ["a", "b", "a", "b", 2, 3]
print(("c", "d") * 2 + (4, 5))      # ("c", "d", "c", "d", 4, 5)

#%% Membership operator (in)
print(" " in "Hello, World!")       # True
print("ello" in "Hello, World!")    # True
print("abc" in "aabbcc")            # False, 'a', 'b', 'c' all occur, but not consecutively
print("bcc" in "aabbcc")            # True, 'bcc' occurs as a substring

print(1 in [1, 2, 3])               # True
print("abc" in ['a', 'b', 'c'])     # False
print("a" in ['abc'])               # False
print(["abc"] in ["abc"])           # False: the RHS contains the string "abc", not a list!
# The same for tuples as for lists.

#%% Methods
print(str.upper("abc"))

#%% Methods
print("abc".upper())        # call str.upper() with "abc" as the subject
                            # i.e. calls str.upper("abc")

#%% Methods
print("abcba".find('b'))          # 1 - the index of the first occurrence of 'b'
print("  a b c  ".strip())        # 'a b c' - with trailing spaces removed
print("abcbcba".split('b'))       # ['a', 'c', 'c', 'a']
print('!'.join(['a', 'b', 'c']))  # 'a!b!c'

#%% The None data type (NoneType)
print(None)
print(type(None))
x = print("abcdef")     # we print "abcdef"
print(x)                # x now has value None

#%% List methods
l = [0, 1, 2, 3]
l.append(4)          # Add element 4 to the end of the list.
l.extend([5, 6, 7])  # Adds all the elements passed to the list.
x = l.pop(0)         # Removes and returns the element at index 0.
l.insert(0, 9)       # Inserts at index 0 the element 9.
l.remove(5)          # Remove the first occurrence of 5, if found.
l.sort()             # Sorts the list in-place. Returns nothing.
l.reverse()          # Reverses the list in-place. Returns nothing.

#%% List methods
l = [3, 2, 1]     # create a list
l = l.sort()      # l.sort() sorts in-place, and returns None.
print(l)          # l is None
l = l.reverse()   # causes an error

#%% List comprehension
# [expression for i in iterable if condition]

# apply f(n) = 2*n for every n in [0, 1, 2, 3, 4]
l = [2*n for n in range(5)]           # [0, 2, 4, 6, 8]

# apply f(c) = c + "1" for every c in "ABC"
l = [c + "1" for c in "ABC"]           # ["A1", "B1", "C1"]

# apply f(x, y) = (x, y) for every x in [1, 2], y in ['A', 'B']
l = [(x, y) for x in [1, 2] for y in ("A", "B")]
# result: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

l = [c for c in "Hello, World!" if c.isupper()]   # ['H', 'W']

#%% Length, indexing, and modifying a dictionary
eg_dict = {"python": "snake", "boa": "snake"}
print(len(eg_dict))      # 2, since there are 2 key-value pairs

#%% Length, indexing, and modifying a dictionary
print(eg_dict["python"])        # Access the value of an existing key

# Modify the value of an existing key
eg_dict["python"] = "programming language"
print(eg_dict["python"])

# Define a new key-value pair
eg_dict["anaconda"] = "big snake"
print(eg_dict["anaconda"])

#%% Membership operator (in)
print("python" in eg_dict)      # True
print("cobra" in eg_dict)       # False
print("big snake" in eg_dict)   # False: that is a value in the dictionary, not a key

#%% Dictionary methods
# Get all key:value pairs in the dictionary
for key, value in eg_dict.items(): print(key, value)

# Get all keys of the dictionary
for key in eg_dict.keys(): print(key)

# Get all values in the dictionary
for value in eg_dict.values(): print(value)

# Update dict with key:value pairs in new_dict
another_dict = {"viper": "poisonous snake!"}
print(eg_dict)
eg_dict.update(another_dict)
print(eg_dict)

print(another_dict)
another_dict.clear()            # Empty the dictionary
print(another_dict)

#%% Iteration
for char in "this is a string":
  print(char, end="")

for e in ["this", "is", "a", "list"]:   # same for tuples
  print(e, end=" ")
