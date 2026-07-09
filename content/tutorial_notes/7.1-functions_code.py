#%% Defining a function (`def`)
def function_name(param1, param2):
  # code to run - here written with `pass` as a placeholder.
  # `pass` does nothing, it exists only to make the code syntactically valid.
  # without it, there would be a syntax error.
  # to see this, just erase the `pass` below.
  pass

#%%
def f(value):
  return 2 * value

print(f(4))       # calls f with value = 4, returns 8
print(f("abc"))   # calls f with value = "abc", returns "abcabc"
f(1, 2)           # error, f() expects only a single input
print(value)      # error, variable `value` is not defined

#%% Return values (`return`)
def f(x):
  return g(x)**2
def g(x):
  return 2*x

print(f(2))     # f(2) -> g(2)**2 -> (2*2)**2 -> 4**2 -> 16

#%% Multiple return values
def f(x):
  return x, x+1

print(f(3))     # (3, 4)
print(f(3)[1])  # 4

#%% Multiple `return` statements
def f(n):
  if n % 2 == 1:
    return "odd"
  else:
    return "even"

print(f(1), f(2))

#%%
def f():
  return 12     # function terminates here
  print("I will never run.")
  return "this will never be reached"

print(f())      # 12

#%% No `return` statements
outs = print()  # get the return value of print()
print(outs)     # and print it. None

def f():
  pass          # function does nothing, has no return statement
print(f())      # None

#%% Ground-up example
string = input("enter a string: ")

count = 0
for char in string:
  if char in 'aeiou':
    count += 1

print("there are", count, "vowels.")

#%%
def count_vowels(string):
  count = 0
  for char in string:
    if char in 'aeiou':
      count += 1
  
  return count

string = input("enter a string: ")
print("there are", count_vowels(string), "vowels.")

# do stuff... 100 lines later

string = input("enter a string: ")
print("there are", count_vowels(string), "vowels.")

