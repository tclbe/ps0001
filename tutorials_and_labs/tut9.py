#%% Q1
def my_add2(n):
    sums = 0 # accumulator variable
    for i in range(n+1): # stop at n (0 irrelevant)
        sums += i # accumulate!
    return sums

for i in range(11):
    print(my_add2(i), end=" ")
    
#%% Q2
def my_add3(start, end, step):
    sums = 0 # accumulator variable
    for i in range(start, end+1, step):
        # include end - so range until end+1
        sums += i # accumulate!
    return sums

print(my_add3(8,88,7))

#%% Q3 - small test
# start with a small test so that you know
# the loop is generating the correct sequence.

# start at 0, difference of 3
# difference increases by 2 at each term.

# initial conditions
term = 0
diff = 3

sums = 0
for i in range(5):
    print(term)
    sums += term
    term += diff # get the next term
    diff += 2    # adjust the difference
print("sum is", sums)

#%% Q3 - full
# make sure you start from the same initial conditions
# since term and diff were modified above.

# initial conditions
term = 0
diff = 3

sums = 0
for i in range(15):
    sums += term
    term += diff
    diff += 2
print(sums)

#%% Q4 - small test
# initial conditions - starting at 'figure 0'
dots = 10
diff = 6

for i in range(1, 31):
    print(f"figure {i} has {dots} dots")
    dots += diff

#%% Q4 - full
# reset initial conditions
dots = 4
diff = 6

for i in range(1, 31):
    dots += diff
print(f"figure 30 has {dots} dots")

#%% Q5 - small test
sums = 0
for i in range(1, 3): # 2 terms
    term = 1 / (i * (i+1))
    print(f"1/({i}*{i+1}) = {term}")
    sums += term
print(sums)

#%% Q5 - full
sums = 0
for i in range(1, 50): # 49 terms
    sums += 1 / (i * (i+1))
print(sums)

# 1/(1*2) = 1/1 - 1/2
# 1/(2*3) = 1/2 - 1/3
# ...
# 1/(i * (i+1)) = 1/i - 1/(i+1)
# ==> sum should be 1 - 1/50 = 0.98
# difference is due to floating point inaccuracies
# (storing decimal, base 10 numbers in binary)

#%% Q6 setup
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# case sensitive!
print(MORSE_CODE_DICT['A'])
print(MORSE_CODE_DICT['E'])
print(MORSE_CODE_DICT['S'])

#%% Q6
# all the below are equivalent
def translate(string):
    translated = "" # accumulator variable
    for c in string.upper():
        translated += MORSE_CODE_DICT[c] + " "
    return translated

user_str = "SOS"
print(f"'{translate(user_str)}' - trailing space")

#%% Q6
def translate(string):
    translated = ""
    for c in string.upper():
        translated += MORSE_CODE_DICT[c] + " "
    return translated.strip() # remove trailing spaces
print(f"'{translate(user_str)}' - stripped space")

#%% Q6 - list comprehension
def translate(string):
    return [MORSE_CODE_DICT[c] for c in string.upper()]
morse = translate(user_str)

print(morse)
print(" ".join(morse))