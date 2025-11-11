import math

help(math)
help(math.log)
help(math.sqrt)
help(math.radians)
help(math.sin)

#%% Task 1
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
a = 4
b = 13
c = 15

s = (a + b + c) / 2

A = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("The area of the triangle is", A)

#%% Task 2
# a = float(input("a: "))
# b = float(input("b: "))
# theta = float(input("theta in degrees: "))

a = 8
b = 10
theta = 90
theta = math.radians(theta)

A = (a * b * math.sin(theta)) / 2
print("The area of the triangle is", A)
