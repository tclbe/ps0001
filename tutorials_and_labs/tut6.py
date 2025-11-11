#%% Easy Q1
my_list = ['abc', True, 123, [3.14, 2.71, 1.61]]
for item in my_list:
    print(type(item))

#%% Easy Q2
my_numbers = []

# my_numbers.append(1)
# my_numbers.append(-1)
# my_numbers.append(2)
# my_numbers.append(-3)
# my_numbers.append(5)
# my_numbers.append(-8)
my_numbers.extend([1, -1, 2, -3, 5, -8])
# for i in [1, -1, 2, -3, 5, -8]:
#     my_numbers.append(i)
print(my_numbers)

#%%
my_numbers.insert(0, 0)
print(my_numbers)

#%%
my_numbers.sort()
print(my_numbers)

#%%
my_numbers.pop()
print(my_numbers)

#%%
my_numbers.reverse()
print(my_numbers)

#%% Easy Q3
money = {"alice": 123, "bob": 456, "eve": 789}

#%%
sum = 0
# Iterate over all of both keys and values
for name, amount in money.items():
    sum += amount
print(sum)

#%%
sum = 0
# Iterate over only the values
for amount in money.values():
    sum += amount
print(sum)

#%%
sum = 0
# Iterate over only all the keys
for name in money:
    # and subsequently access the values by indexing.
    sum += money[name]
print(sum)

#%% Easy Q4
stringy = input("enter a string: ")
letter = input("enter a letter: ")

#%%
stringy = "abcdefedcba"
letter = "d"

for i in range(len(stringy)):
    if stringy[i] == letter:
        index = i
        break
else:
    index = -1

if index == -1:
    print("letter not found!")
else:
    print(stringy[:index + 1])
    print(stringy[index + 1:])

#%%
stringy = "abcdefedcba"
letter = "d"

index = stringy.find(letter)

if index == -1:
    print("letter not found!")
else:
    print(stringy[:index + 1])
    print(stringy[index + 1:])

#%% Easy Q5
squares = []
for i in range(1, 11):
    squares.append(i**2)

squares2 = [x**2 for x in range(1, 11)]

#%% Easy Q6
me = {'name': 'Caleb', 'age': 26}
me['enjoyment'] = 5
print(me['name'], "is", me['age'], "years old and has an enjoyment score of",
      me['enjoyment'])

#%% Medium Q1
names = ['Alice', 'Bob', 'Carlos', 'Dave', 'Eve']
selection = [name for name in names if name[-1] == 'e']

#%% Medium Q2
dice_pairs = []
for i in range(1, 7):
    for j in range(1, 7):
        dice_pairs.append((i, j))
print(len(dice_pairs))

dice_pairs2 = [(i, j) for i in range(1, 7) for j in range(1, 7)]
print(len(dice_pairs2))

#%% Medium Q3
unordered_dice_pairs = []
for i in range(1, 7):
    for j in range(1, 7):
        if i <= j:
            unordered_dice_pairs.append((i, j))
print(len(unordered_dice_pairs))

unordered_dice_pairs2 = [(i, j) for i in range(1, 7) for j in range(1, 7)
                         if i <= j]
print(len(unordered_dice_pairs2))

#%%
unordered_dice_pairs = []
for i in range(1, 7):
    for j in range(i, 7):
        unordered_dice_pairs.append((i, j))
print(len(unordered_dice_pairs))

unordered_dice_pairs2 = [(i, j) for i in range(1, 7) for j in range(i, 7)]
print(len(unordered_dice_pairs2))

#%% Medium Q4
l1 = ['q', 1, 'w', 2]
l2 = [x * 2 for x in l1]
print(l2)

#%% Medium Q5
listy = ["qwer", "asdf", "zxcv"]
for i in range(len(listy)):
    print(i, listy[i][i], end=" ")

#%% Medium Q6
stringy = input("Enter a string: ")
to_remove = input("Enter letters to remove: ")

#%%
stringy = "cut through the night"
to_remove = "aeiou"

out = ""
for c in stringy:
    if c not in to_remove:
        out += c

print(out)

#%%
stringy = "cut through the night"
to_remove = "aeiou"

out_list = [c for c in stringy if c not in to_remove]
print(out_list)
print("".join(out_list))

#%% Medium Q7
string = input("enter a string: ")

out = ""
for i in range(len(string)):
    c = string[i]
    if i % 2 == 0: out += c.lower()
    else: out += c.upper()
print(out)

out2 = [
    string[i].lower() if i % 2 == 0 else string[i].upper()
    for i in range(len(string))
]
print(out2)

#%% Alternatively, with enumerate():
# enumerate() pairs each value with its index
# in the order of (index, value)
out = ""
for i, c in enumerate(string):
    if i % 2 == 0: out += c.lower()
    else: out += c.upper()
print(out)

out2 = [c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(string)]
print(out2)
