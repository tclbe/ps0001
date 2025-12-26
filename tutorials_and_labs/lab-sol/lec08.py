#%% string reverse
def reverse(a_str):
    print(f"reverse('{a_str}') called")
    # base case
    if len(a_str) == 1:
        print(f"base case. reverse('{a_str}') = {a_str}")
        return a_str
    # recursive step
    else:
        first_char = a_str[0]
        substr = a_str[1:]
        returned = reverse(substr)
        new_str = returned + first_char
        print(f"recursive. reverse('{a_str}') = {new_str}")
        return new_str

#%%
reverse("abc") # = reverser("bc") + 'a'
# so python has to evaluate what reverser("bc") is.
# reverser("bc") = reverser("c") + 'b'
# so python has to evaluate what reverser("c") is.
# this falls into the base case, so:
# reverser("c") = 'c'
# therefore,
# reverser("bc") = reverser("c") + 'b' = 'c' + 'b' = "cb"
# therefore,
# reverser("abc") = reverser("bc") + 'a' = "cb" + 'a' = "cba"

#%% decomposition
# fibonacci
# f(n) = f(n-1) + f(n-2), n > 3
# f(1) = f(2) = 1
def fib(n):
    # base cases
    if n == 1 or n == 2:
        return 1
    # recursive definition
    elif n > 2:
        return fib(n-1) + fib(n-2)

def fib_timeit(n):
    import time
    now = time.time()
    fib(n)
    return time.time() - now

#%%
print(fib(0))

#%%
old = fib_timeit(24)
for i in range(25, 41):
    timing = fib_timeit(i)
    print(f"fib({i}) took {timing:.3f} seconds. increase of {timing/old:.3f}x")
    old = timing

#%% without error handling
# x = float(input("x: "))
x = float("abc")
print(f"f({x}) = {x**2}")

#%%
x = input("x: ")
if x.isnumeric():
    x = float(x)

#%% try-except - specific error
try:
    x = float(input("x: "))
    # x = float("abc")
    print(f"f({x}) = {x**2}")
except:
    print("Please enter a number!")

#%% try-except - specific error
try:
    # x = float(input("x: "))
    x = float("123")
    print(f"f({a}) = {a**2}")
except ValueError:
    # If there is a ValueError; run this.
    print("Please enter a number!")
    
#%% try-except - specific error AND catch-all error
try:
    # x = float(input("x: "))
    x = float("123")
    print(f"f({a}) = {a**2}")
except ValueError:
    print("Please enter a number!")
except TypeError:
    # If there is a TypeError; run this.
    print("TypeError")
except:
    # If there is an error that was not a ValueError or a TypeError; run this.
    print("Unexpected error")


#%% try-except does not save you from syntax errors.
print("i ran!")
try:
    x = float(input("x: "))
    print(a)
except:
    print("syntax error")
finally:
    print(()

#%% while-try-except
while True:
    try:
        x = float(input("x: "))
        print(f"f({x}) = {x**2}")
    except ValueError:
        print("Please enter a number!")
    except:
        print("Unexpected error")
    else:
        break

#%% try-except-else-finally
try:
    # x = float(input("x: "))
    x = float("abc")
except ValueError:
    print("Please enter a number!")
else:
    print(f"f({x}) = {x**2}")
finally:
    print("finally!")

#%% while-try-except-else-finally
while True:
    try:
        x = float(input("x: "))
    except ValueError:
        print("Please enter a number!")
    except:
        print("Unexpected error")
        break
    else:
        print(f"f({x}) = {x**2}")
        break
    finally:
        print("finally!")
