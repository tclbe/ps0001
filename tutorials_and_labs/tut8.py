# %% q1
# sum of numbers 1, ..., n
def my_add(n):
    # base case
    if n == 0:
        return 0
    # recursive definition
    elif n > 0:
        return n + my_add(n - 1)

# 
for i in range(11):
    print(my_add(i), end=" ")


# %% q2
def my_factorial(n):
    # base case
    if n == 0:
        return 1
    # recursive definition
    else:
        return n * my_factorial(n - 1)


# f-strings, to format variables into strings.
# prefixed with f, i.e. f"<string contents>"
# insert variables to print into curly braces {}
for i in range(11):
    print(f"{i}! = {my_factorial(i)}")

# %% q3


def gcd(a, b):
    # make such that a >= b always
    if b > a:
        a, b = b, a

    r = a % b

    # base cases
    if r == 0:
        return b
    elif r == 1:
        return 1

    # recursive definition
    else:
        return gcd(b, r)


print(gcd(13, 385))


# %% q4
def my_rfibo(n):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive definition
    elif n > 1:
        return my_rfibo(n - 1) + my_rfibo(n - 2)


for i in range(11):
    print(my_rfibo(i), end=" ")


# %% q5
def my_ifibo(n):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # iterative
    elif n > 1:
        f1 = 0
        f2 = 1
        for i in range(n - 1):
            f1, f2 = f2, f1 + f2
        return f2


for i in range(11):
    print(my_ifibo(i), end=" ")


# %% q6
def rfib_timeit(n):
    import time
    now = time.time()
    my_rfibo(n)
    return time.time() - now


def ifib_timeit(n):
    import time
    now = time.time()
    my_ifibo(n)
    return time.time() - now

#%%
print("ITERATIVE")
for i in range(800, 805):
    timing = ifib_timeit(i)
    print(f"ifib({i}) took {timing:.3f} seconds.")

#%%
print("RECURSIVE")
old = rfib_timeit(30)
for i in range(31, 36):
    timing = rfib_timeit(i)
    print(
        f"rfib({i}) took {timing:.3f} seconds. increase of {timing/old:.3f}x")
    old = timing

# %%
# using caching (out of syllabus):
# using the below code, python automagically
# stores the return values of my_rfibo(n).
# so that it doesn't have to repeatedly
# *compute* the values.
# instead, python can just look up what the
# return value is (since it stored it).

from functools import lru_cache


@lru_cache(100)
def my_rfibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_rfibo(n - 1) + my_rfibo(n - 2)


print("CACHED RECURSIVE")
for i in range(800, 805):
    timing = rfib_timeit(i)
    print(f"rfib({i}) took {timing:.3f} seconds.")

# you could also define new base cases.

# %% q8


def is_palindrome(string):
    # base cases
    # if string is length 0 or 1, it must be palindromic.
    if len(string) <= 1:
        return True
    # if first and last characters are NOT the same,
    # then it is NOT palindromic.
    elif string[0] != string[-1]:
        return False

    # recursive - note that it is either that
    # the first and last characters are the same,
    # or that they are not the same.
    elif string[0] == string[-1]:
        # if the first and last letters are the same,
        # it COULD be palindromic, depending on the
        # inside characters.
        substr = string[1:-1]
        return is_palindrome(substr)


print(is_palindrome("rotor"))
# is_palindrome("rotor")
# is_palindrome("oto")
# is_palindrome("t") => True

print(is_palindrome("rottor"))

print(is_palindrome("rovtor"))
# is_palindrome("rovtor")
# is_palindrome("ovto")
# is_palindrome("vt") => False

print(is_palindrome("accab"))
# is_palindrome("accab") => False

print(is_palindrome("abba"))
