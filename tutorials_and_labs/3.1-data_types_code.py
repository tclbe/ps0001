#%% Python comments
''' An example of a multiline comment
"Programs must be written for people to read, and only incidentally for machines to execute."
- Harold Abelson & Gerald Jay Sussman
''' 
module = "PS0001"     # Introduction to Computational Thinking
lab = 3               # Week 3
author = "Caleb Tay"  # :)
print("Hello, and welcome to", module, "lab", lab)
#print("I am commented out. I don't run.")
print("This lab was written and developed by", author)

#%% Integers (`int`)
print("12+34 =", 12+34) # an int
print("56-78 =", 56-78) # an int
print("12*89 =", 12*89) # an int
print("34/67 =", 34/67) # a float

#%% Strings (`str`)
first = 'this is a stirng'
second = "this is also a string"
third = '''i am
a multi-line
string'''
print(third)

#%% The `type()` function
print(type(123))   # int
print(type(123.0)) # float
print(type("123")) # str (a string of numbers)

#%% Implementing user interactivity - the `input()` function
print("Hello!")
input("press a key.")
print("World!")

#%%
your_name = input("What is your name? ")
print("Hello, it is nice to meet you,", your_name)

#%%
your_age = input("What is your age? ")
print("You will be", your_age + 2, "years old in 2 years time.")

#%%
three = '3'
print("3 times 3 is", three * 3)
three = int(three)
print("3 times 3 is", three * 3)

#%%
your_age = int(input("What is your age? "))
print("You will be", your_age + 2, "years old in 2 years time.")

#%%
float("3") + 2
int("3") + 2
float("3.14159") + 2
int("3.14159") + 2

#%% `NameError`
x = 12
print(a)

#%% Use of keywords as variable names
import = 0

#%% Improper indentation
print("Hello!")
 print("World!")

#%% Unmatched brackets
print())

