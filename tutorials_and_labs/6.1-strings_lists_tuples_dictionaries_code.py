#%% The `len()` function
print(len("Hello, World!"))   # 13 characters
print(len(""))                # 0 characters

#%% Indexing
x = "Hello, World!"
print(x[0])     # character at the 0th index, 'H'
print(x[4])     # character at the 4th index, 'o'
print(x[-1])    # character at the -1th index, '!'

#%% Slicing
print(x[0:3])     # characters between index 0 and 3, "Hel"
print(x[:6])      # characters until index 6, "Hello,"
print(x[-6:])     # characters from index -6, "World!"
print(x[-10:10])  # characters between index -10 and 10, "lo, Wor"
print(x[::-1])    # characters in the string backwards, "!dlroW ,olleH"

#%% Arithmetic operators on strings
print("abc" + "def" + "ghi")
print("abc" * 2 + 2 * "def")

#%% Membership operator (`in`)
print(" " in "Hello, World!")     # True
print("ello" in "Hello, World!")  # True
print("abc" in "aabbcc")          # False, 'abc' does not occur.
print("abc" in "aabcc")           # True

#%% String methods
print("abc".upper())      # upper() acts on "abc", results in "ABC"
print("pqr".upper())      # upper() acts on "pqr", results in "PQR"

#%%
print("abcba".find('b'))          # 1 - the index of the first occurrence of 'b'
print("  a b c  ".strip())        # 'a b c' - with trailing spaces removed
print("abcbcba".split('b'))       # ['a', 'c', 'c', 'a']
print('!'.join(['a', 'b', 'c']))  # 'a!b!c'

#%% Immutability of strings
x = "immutable"
#x[3] = "c"               # causes an error
y = x[:2] + "c" + x[3:]   # "imcutable"

#%% Lists
l = list('abc')               # must be some iterable object
l = ['a', 'b', 'c']           # the above line makes the same list
l = [1, 3.14159, 'a', True]   # can contain different types
print(len(l))                 # 4 items in the list.

#%% Indexing, slicing
print(l[0])     # element at 0th index
print(l[:2])    # elements until 2nd index
print(l[-3:2])  # elements from -3th index to 2nd index

#%% Arithmetic operators on lists
print(["abc"] + ["def"] + ["ghi"])
print(["abc"] * 2 + 2 * ["def"])

#%% Membership operator (`in`)
print(1 in [1, 2, 3])             # True
print("abc" in ['a', 'b', 'c'])   # False
print("a" in ['abc'])             # False

#%% Mutability of lists
l = [0, 1, 2, 3]
print(l)          # [0, 1, 2, 3]
l[2] = 8          # change the 2nd index to be 8
print(l)          # [0, 1, 8, 3]

#%% List methods
list.append(e)         # Add element e to the end of the list.
list.extend(iterable)  # Adds all the elements passed to the list.
x = list.pop(i)        # Removes and returns the element at index i.
list.insert(i, e)      # Inserts before index i the element e.
list.remove(e)         # Remove the first occurrence of e, if found.
list.sort()            # Sorts the list in-place. Returns nothing.
list.reverse()         # Reverses the list in-place. Returns nothing.

#%%
l = [3, 2, 1]     # create a list
l = l.sort()      # l.sort() sorts in-place, and evaluates to None.
print(l)          # l is None
l = l.reverse()   # causes an error

#%% Tuples
t = (1, 2, 3)     # create a tuple
print(len(t))     # 3
print(t[0])       # 1
#t[1] = 4         # causes an error
#t.append(4)      # causes an error

#%% List comprehension
# [expression for i in iterable if condition]

# apply f(n) = 2*n for every n in [0, 1, 2, 3, 4]
l = [2*n for n in range(5)]           # [0, 2, 4, 6, 8]

# apply f(c) = ord(c) for every c in ['A', 'B', 'C']
l = [ord(c) for c in "ABC"]           # [65, 66, 67]

# apply f(x, y) = (x, y) for every x in [1, 2], y in ['A', 'B']
l = [(x, y) for x in [1, 2] for y in ("A", "B")]
# result: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

l = [c for c in "Hello, World!" if c.isupper()]   # ['H', 'W']

#%% Dictionaries
dollars = {'alice': 839, 'bob': 1098, 'eve': 373}
dollars['caleb'] = 4    # add a new entry

#%% Membership operator (`in`)
print('alice' in dollars)   # True
print('bobby' in dollars)   # False
print(839 in dollars)       # False: 839 is a value, not a key

#%% Dictionary methods
dict.items()            # Get all key:value pairs in the dictionary
dict.keys()             # Get all keys of the dictionary
dict.values()           # Get all values in the dictionary
dict.clear()            # Empty the dictionary
dict.update(new_dict)   # Update dict with key:value pairs in new_dict

#%% Iteration
for char in "this is a string":
  print(char, end="")
for e in ["this", "is", "a", "list"]:   # same for tuples
  print(e, end=" ")
for k in {"key": "value", "dictionary": "pair"}:
  print(k)

