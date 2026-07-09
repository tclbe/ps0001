#%% Easy Q1
import math


def f(x, y, z):
    return x & y + math.sin(y * z) + x * z * math.pi


#%% Easy Q2 - without a function
n = 9

if n % 2 == 1:
    print('n is odd')
else:
    print('n is even')


#%%
def is_odd(n):
    return n % 2 == 1
    # if n % 2 == 1:
    #     return "odd"
    # else:
    #     return "even"


print(is_odd(9))

assert is_odd(9) == True, "9 is an odd number."
assert is_odd(143) == True


#%% Easy Q3
def cap_and_rev(string):
    # could do either first, or both simultaneously.
    # for simplicity, uppercase first.
    string = string.upper()
    out = ""

    # iterate over all indexes backwards and construct it.
    for i in range(len(string) - 1, -1, -1):
        char = string[i]
        out += char
    return out


assert cap_and_rev("abc") == "CBA"
assert cap_and_rev("z1Y2x") == "Z2Y1X"


#%% without a for loop.
def cap_and_rev(string):
    string = string.upper()  # capitalise
    string = string[::-1]  # reverse
    return string


assert cap_and_rev("abc") == "CBA"
assert cap_and_rev("z1Y2x") == "Z2Y1X"

#%% Easy Q4 - without a function
n = 9

sums = 0
for i in range(1, n + 1):
    sums += i
print(sums)


#%%
def sum_to(n):
    sums = 0
    for i in range(1, n + 1):
        sums += i
    return sums


assert sum_to(9) == 45
assert sum_to(11) == 66


#%% Medium Q1
def remove_numbers(string):
    out = ""
    for char in string:
        if char not in "1234567890":
            out += char
    return out


print(remove_numbers("asdf123bcde456"))


#%% Medium Q2
def find_max(listy):
    curr_max = listy[0]
    for num in listy:
        if num > curr_max:
            curr_max = num
    return curr_max


def find_min(listy):
    curr_min = listy[0]
    for num in listy:
        if num < curr_min:
            curr_min = num
    return curr_min


print(find_max([3, 5, 4, 9, 1, 2]))
print(find_min([3, 5, 4, 9, 1, 2]))


#%% Medium Q3
def combine_strings(string1, string2):
    out = ""

    # find the length of the shorter string
    length1 = len(string1)
    length2 = len(string2)
    min_length = min(length1, length2)

    # iterate over both strings to alternate between them
    for i in range(min_length):
        out += string1[i] + string2[i]

    # then add whatever is left over.
    # one of them will be an empty string
    out += string1[min_length + 1:]
    out += string2[min_length + 1:]

    return out


assert combine_strings("abcde", "xyz") == "axbyczde"
assert combine_strings("123", "456") == "142536"


#%% Medium Q4 - replica of lab5
def caesar_encode(plaintext):
    plaintext = plaintext.upper()
    ciphertext = ""

    for p in plaintext:
        # Get ASCII value.
        p = ord(p)
        # Minus 65 to get the corresponding value between 0 and 25.
        p = p - ord('A')
        # Encode using the Caesar Cipher.
        c = (p + 1) % 26
        # Add back 65 to get the corresponding value between 65 and 90.
        c = c + ord('A')
        # Convert this number back to the corresponding ASCII character.
        c = chr(c)
        ciphertext += c

    return ciphertext


assert caesar_encode("ABYZ") == "BCZA"


#%%
def shift_encode(plaintext, offset):
    plaintext = plaintext.upper()
    ciphertext = ""

    for p in plaintext:
        p = ord(p)
        p = p - ord('A')
        c = (p + offset) % 26
        c = c + ord('A')
        c = chr(c)
        ciphertext += c

    return ciphertext


def caesar_encode(plaintext):
    return shift_encode(plaintext, 1)


def caesar_decode(ciphertext):
    return shift_encode(ciphertext, -1)


assert caesar_encode("ABYZ") == "BCZA"
assert caesar_decode("ABYZ") == "ZAXY"
