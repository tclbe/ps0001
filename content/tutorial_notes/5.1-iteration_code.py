#%% `while` loops
while (condition is True):
  print("looping")
  # do stuff

#%%
i = 0
while i < 3:
  print("i =", i, end=".")
  i += 1
  print("i increased. i =", i)
print("while loop exited")

#%% `range(end)`
print(range(5))       # will just display range(5)
# to print the contents of the range, we will convert it into a list.
print(list(range(5))) # [0, 1, 2, 3, 4]

#%% `range(start, end)`
print(list(range(3, 9))) # [3, 4, 5, 6, 7, 8]

#%% `range(start, end, step)`
print(list(range(3, 9, 2)))  # [3, 5, 7]
print(list(range(9, 3, -2))) # [9, 7, 5]

#%% `for` loops
for variable in iterable:
  print("looping")
  # do stuff

#%%
for i in range(5):              # iterate over each value in a range
  print(i, end=" ")             # 0 1 2 3 4
for c in "ABCdef":              # iterate over each character in a string
  print(c, end=" ")             # A B C d e f
for item in [123, "456", 789]:  # iterate over each element in a list
  print(item, end="!")          # 123!456!789

#%% `break` statement
for i in range(5):        # iterate over i = 0, 1, 2, 3, 4
  if i == 2:              # exits loop when i == 2,
    break                 # preventing loop execution with i = 3, 4
  print(i, end=" ")       # prints 0 1
print("exited loop")

#%% `else` statement
for i in range(5):
  if i == 2:
    break                 # exits loop when i == 2
  print(i, end=" ")       # prints 0 1
else:
  print("else block")     # not printed
print("exited loop")      # prints

#%% `continue` statement
for i in range(5):
  if i == 2:
    continue              # skips iteration when i == 2
  print(i, end=" ")       # prints 0 1 3 4
else:
  print("else block")     # prints
print("exited loop")      # prints

#%% Nested loops
prod_sum = 0
for i in range(1, 4)
  for j in range(5, 8):
    prod_sum += i * j
print(prod_sum)

