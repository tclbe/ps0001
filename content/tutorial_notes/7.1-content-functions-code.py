#%% Defining a function (def) and its return value (return)
user_in = input("enter a string: ")

vowels = 0
for char in user_in.lower():
  if char in "aeiou":
    vowels += 1
print("there are", vowels, "vowels.")

#%% Defining a function (def) and its return value (return)
def count_vowels(my_string):                # (1)
  vowels = 0
  for char in my_string.lower():
    if char in "aeiou":
      vowels += 1
  return vowels                             # (2)

user_in = input("enter a string: ")
num_vowels = count_vowels(user_in)          # (3)
print("there are", num_vowels, "vowels.")

#%% Scope - local and global variables
def count_vowels(my_string):
  vowels = 0
  for char in my_string.lower():
    if char in "aeiou":
      vowels += 1
  return vowels

count_vowels("hello")
print(vowels)

#%% Scope - local and global variables
greeting = "hello"                  # defined in the global scope

def greet(name):
  return greeting + ", " + name     # uses global variable `greeting`

print(greet("world"))               # "hello, world"

#%% Composability
# Count vowels in multiple words
words = ["strong", "green", "omnibus"]
n_vowels = [count_vowels(word) for word in words]
print(n_vowels)

# Usage in another function...
def vowel_proportion(word):
  if len(word) == 0: return 0.0
  return count_vowels(word) / len(word)
print(vowel_proportion("computational"))

# ... which is used in another different context.
vowelly_words = [word for word in words if vowel_proportion(word) >= 0.4]
print(vowelly_words)

#%% No return statement
def count_vowels(my_string):
  vowels = 0
  for char in my_string.lower():
    if char in "aeiou":
      vowels += 1
  # return vowels

user_in = input("enter a string: ")
num_vowels = count_vowels(user_in)
print("there are", num_vowels, "vowels.")

#%% Multiple return statements
def f():
  print("returning 1!")
  return 1
  print("this will never be printed!")
  return 2

f()

#%% Multiple return statements
def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

#%% Multiple return statements
def is_even(n):
  if n % 2 == 0:
    return True
  # what is returned if n is odd?

#%% Returning multiple values
import math

def polar_coord(r, theta):
  return r * math.cos(theta), r * math.sin(theta)

coord = polar_coord(1, 0.78539816)   # r = 1, theta = pi/4
print(coord)
print(coord[0], coord[1])

# Deconstruct the return value
x, y = polar_coord(1, 0.78539816)    # r = 1, theta = pi/4
print(x, y)
