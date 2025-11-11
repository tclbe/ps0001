#%% Easy Q2 Original
sums = 0
for i in range(10):
    sums += i
print(sums)

#%% Easy Q2
sums = 0
i = 0
while i < 10:
    sums += i
    i += 1
print(sums)

#%% Easy Q3 Original
i = 0
while i < 100:
    print(i, end=" ")
    i += 7

#%% Easy Q3
for i in range(0, 100, 7):
    print(i, end=" ")

#%% Easy Q4
out = ""
for c in "ABCDEFG":
    if c == "C": continue
    out += c
    if c == "E": break
else:
    print("else")
print(out)

#%% Easy Q5
string = input("enter a string: ")
for c in string:
    print(c, end=" ")

#%% Medium Q2
user_in = input("enter a string (':q' to exit): ")
while user_in != ':q':
    vowels = 0
    for c in user_in:
        if c in 'aeiou':
            vowels += 1
    print("there are", vowels, "vowel(s).")
    user_in = input("enter a string (':q' to exit): ")

#%% using while True loop
user_in = input("enter a string (':q' to exit): ")
while True:
    if user_in == ':q': break
    vowels = 0
    for c in user_in:
        if c in 'aeiou':
            vowels += 1
    print("there are", vowels, "vowel(s).")
    user_in = input("enter a string (':q' to exit):")

#%% Medium Q3
import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != number:
    if number > guess:
        print("The number is higher.")
    elif number < guess:
        print("The number is lower.")
    guess = int(input("Guess a number between 1 and 100: "))
print("Congratulations, you guessed the number!")

#%% Medium Q4

import math

n = 1
est = (1 + 1 / n)**n

# while abs(est - math.e) >= 1e-6:
# while abs(est - math.e) >= 0.000001:
while abs(est - math.e) >= 10**-6:
    # est = (1 + 1 / n)**n
    n += 1
    est = (1 + 1 / n)**n

print(n)
