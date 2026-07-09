#%% Booleans (`bool`)
x = True
print(x)
y = False
print(y)

#%% Boolean operators - `and`, `or`, and `not`
print(True and False)   # False
print(False or False)   # False
print(not True)         # False

#%% Relational operators
x = 1
print("1" == x)     # False - they are not the same data type.
print(1 == x)       # True
print(2 != x)       # True
print("A" < "B")    # True - you can compare strings.

#%% Chained relational operators
print(-1 < x < 1)   # equivalent to (-1 < x) and (x < 1)

#%% `if` statements
expression1 = True

if expression1:
  # code to run if expression1 is True
  print("I ran because expression1 was true.")

#%% `if-else` statements
expression1 = True

if expression1:
  # code to run if expression1 is True
  print("I ran because expression1 was true.")
else:
  # code to run if expression1 is False
  print("I ran because expression1 was false.")

#%%
expression1 = True
expression2 = True

if expression1:
  # code to run if expression1 is True
  print("I ran because expression1 was true.")
else:
  print("I ran because expression1 was false.")
  if expression2:
    # code to run if expression1 is False and expression2 is True
    print("I ran because expression1 was false, and expression2 was true.")
  else:
    # code to run if both expression1 and expression2 are False
    print("I ran because expression1 was false, and expression2 was false.")

#%% `if-elif` statements
expression1 = True
expression2 = True

if expression1:
  # code to run if expression1 is True
  print("I ran because expression1 was true.")
elif expression2:
  # code to run if expression1 is False and expression2 is True
  print("I ran because expression1 was false, and expression2 was true.")

#%% `if-elif-else` statements
expression1 = True
expression2 = True

if expression1:
  # code to run if expression1 is True
  print("I ran because expression1 was true.")
elif expression2:
  # code to run if expression1 is False and expression2 is True
  print("I ran because expression1 was false, and expression2 was true.")
else:
  # code to run if both expression1 and expression2 are False
  print("I ran because both expression1 and expression2 were false.")

#%% Short-circuiting
expression1 = True

if expression1 or 1 / 0:
  # True or (whatever)
  print("I can still run despite dividing by zero.")

#%% `if-elif-else` example
x = -1                            # line 1
if x > 0:                         # line 2: x is -1, so x > 0 is False
  print("x is positive")          # line 3: not run, does not print
elif x < 0:                       # line 4: x is -1, so x < 0 is True
  print("x is negative")          # line 5: prints, short circuits
else:                             # line 6: not run
  print("x is 0")                 # line 7
print("the value of x is", x)     # line 8: prints

#%% Exponentiation (`**`)
print("10 ** 3 is", 10 ** 3)   # 1000, since 10^3 = 1000
print("22 ** 5 is", 22 ** 5)   # 5153632, since 22^5 = 5153632

#%% Modulo (`%`)
print("10 % 3 is", 10 % 3)     # 1, since 10 / 3 = 3 **remainder 1**
print("22 % 5 is", 22 % 5)     # 2, since 22 / 5 = 4 **remainder 2**

#%% Floor division (`//`)
print("10 // 3 is", 10 // 3)    # 3, since 10 / 3 = **3** remainder 1
print("22 // 5 is", 22 // 5)    # 4, since 22 / 5 = **4** remainder 2

#%% Shorthand arithmetic assignment
x = 0
x += 1     # equivalent to x = x + 1

