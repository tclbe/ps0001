#%% Easy Q1
import math

print((math.pi**3 - 5.6**2 + 1) /  # Numerator
      (1.2**(math.pi / 2) - math.log(465**math.e)) +  # Denominator
      (14.8 / math.e)**(math.pi - 1.8))

#%% Easy Q2
# a
3 == 2 + 1
3 == (2 + 1)
3 == 3
True

# b
7 < 6 or 8 > 4
False or 8 > 4
False or True
True

# c
False and True or not False
False and True or (not False)
False and True or True
(False and True) or True
False or True
True

#%% Easy Q3
color = 'red'
shape = 'circle'
if color == 'red' and shape == 'square':
    print("Red square")
elif color == 'blue' or shape == 'circle':
    print("Blue or a circle")
elif color == 'red' and shape == 'circle':
    print("Red circle")
else:
    print("Something else")

#%% Easy Q4
number = int(input("enter a number: "))
if number % 2 == 1:
    print(number, "is an odd number.")
else:
    print(number, "is an even number.")

#%% Easy Q5 - if-elif-else
ph = float(input("Enter pH of solution: "))
if 0 <= ph < 7:
    print("The solution is acidic.")
elif ph == 7:
    print("The solution is neutral.")
elif 7 < ph <= 14:
    print("The solution is basic.")
else:
    print("Invalid pH. pH should be between 0 and 14.")

#%% Easy Q5 - nested ifs
ph = float(input("Enter pH of solution: "))
if 0 <= ph < 7:
    print("The solution is acidic.")
else:
    if ph == 7:
        print("The solution is neutral.")
    else:
        if 7 < ph <= 14:
            print("The solution is basic.")
        else:
            print("Invalid pH. pH should be between 0 and 14.")

#%% Medium Q1
bool("")
bool("False")

bool(-1)
bool(0)
bool(1)
bool(-1 and 0)

bool(-1.1)
bool(0.0)
bool(1.1)

int(True)
int(False)
float(True)
float(False)

(True * 2)**2 // 2
(False + 2)**2 // 2

#%% Medium Q2 original
# letter = input("enter a letter: ")
# if letter = 'a' or 'e' or 'i' or 'o' or 'u':
#     print(letter, "is a vowel")

#%% Medium Q2 final
letter = input("enter a letter: ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, "is a vowel")

#%% alternative - seen in week 6
letter = input("enter a letter: ")
if letter in 'aeiou':
    print(letter, "is a vowel")

#%%
original_hours = 12345
years = original_hours // (24 * 365)  # there are 24*365 hours in a year.
days = original_hours // 24 % 365  # floor divide by 24 for days in 12345 hours.
hours = original_hours % 24  # modulo by 24 for number of hours leftover.
print(original_hours, "hours is equal to", years, "year(s),", days,
      "days, and", hours, "hours.")

#%% Medium Q4
numgrade = float(input("Input a numerical grade from 0 to 10:"))
if numgrade >= 9:
    print("A!")
elif numgrade >= 8:
    print("B")
elif numgrade >= 7:
    print("C")
elif numgrade >= 6:
    print("D")
elif numgrade >= 5:
    print("E")
else:
    print("F")

#%% Medium Q5
distance = float(input("Enter distance in kilometers: "))

if 0 <= distance <= 20:
    print("Walking is free!")
else:
    print("Too far to walk!")

if 0 <= distance <= 200:
    print("Cost of travel by motorcycle: ", round(distance * 0.22, 2))
else:
    print("Too far to travel by motorcycle!")

if 0 <= distance <= 800:
    print("Cost of travel by car: ", round(distance * 0.26, 2))
else:
    print("Too far to travel by car!")

if distance >= 100:
    print("Cost of travel by plane: ", round(distance * 0.76, 2))
else:
    print("Too close to travel by plane!")

#%% Extra Q5
print("Quadratic solver: ax^2 + bx + c = 0")
print("Enter values for a, b, c:")
a = input("a: ")
b = input("b: ")
c = input("c: ")

a = float(a)
b = float(b)
c = float(c)

discr = b**2 - 4 * a * c

if discr < 0:
    print("No real roots.")
elif discr == 0:
    root = (-b / (2 * a))
    print("The root is", root)
else:
    import math
    root1 = (-b + math.sqrt(discr)) / (2 * a)
    root2 = (-b - math.sqrt(discr)) / (2 * a)
    print("The roots are", root1, "and", root2)
