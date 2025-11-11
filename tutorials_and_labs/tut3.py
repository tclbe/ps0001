#%% Easy Q1
my_float = 2.0
my_int = 2
my_str = "2"

print(my_float, type(my_float))
print(my_int, type(my_int))
print(my_str, type(my_str))

#%% Easy Q2
quote = '"Programs are meant to be read by humans and only incidentally for computers to execute." - Donald E. Knuth'
print(quote)

#%% Easy Q3 - Initial
# q3 = "'''what"""a'''troublesome"""string"


#%% Easy Q3 - Final
q3 = "'''what\"\"\"a'''troublesome\"\"\"string"
print(q3)

#%% Easy Q4 - Original
# x = input("enter value for x: ")
# print("3*x is", "3*x")
# print("x*x is", "x*x')
# print("(x+2)^2 is", '(x+2)**2')

#%% Easy Q4 - Fixed
x = input("enter value for x: ")
x = float(x)
print("3*x is", 3*x)
print("x*x is", x*x)
print("(x+2)^2 is", (x+2)**2)


#%% Easy Q5 - Initial
user_age = input("enter your age: ")
user_age = user_age - 5
print("Five years ago, you were", user_age, "years old.")

#%% Easy Q5 - Final
user_age = int(input("enter your age: "))
user_age = user_age - 5
print("Five years ago, you were", user_age, "years old.")
user_age = user_age + 8
print("In 3 years, you will be", user_age, "years old.")

#%% Easy Q6
r1 = 3
r2 = 2.2
r3 = 1.5
rt = 1 / ( (1 / r1) + (1 / r2) + (1 / r3) )
print(rt)

#%% Medium Q1
"abc" + "123"
"asdf" - "123"
"123" * "ABC"
"asdfg" / "12345"

#%% Medium Q2
"a" + 1
"123" - 1
123 - "asdf"
"123" * 3
"123" / 3
123 / "asdf"

#%% Medium Q3
a = d
c = 10
a = c + 1
a + c = c
3 + a
7up = 10
import = 1003
int = 500
a ** 3
b = math.pi * c
a,b,c = c,1,a
b,c,a = a,b
c = b = a = 7
print(A)
print("b*b + a*a = c*c")

#%% Medium Q5 - Initial
length = int(input("length: "))
width = int(input("width: "))

perimeter = length + width + length + width
area = length * width

print("perimeter:", perimeter)
print("area:", area)


#%% Medium Q4 - Original
# temperature = 35
# wind speed = 11
# wcf = (35.7 + 0.6)T - 35.7(V^{0.16}) + (0.43*T*(V**0.16)))
# print("The temperature is", T, "and wind speed is", V)
# print("The wind chill factor is", "wcf")

#%% Medium Q4 - Fixed
T = 35
V = 11
wcf = 35.7 + 0.6 * T - 35.7*(V**0.16) + (0.43*T*(V**0.16))
print("The temperature is", T, "and wind speed is", V)
print("The wind chill factor is", wcf)

#%% Medium Q5
length = float(input("length: "))
width = float(input("width: "))

perimeter = length + width + length + width
area = length * width

print("perimeter:", perimeter)
print("area:", area)
