#%% Time complexity
# Basically, how long a function takes to run with a given size of input.

# For example, we have different functions that take
# 2^n seconds to run,
# n^2 seconds to run,
# n seconds to run, and
# log n seconds to run

# Size of input |   1 |   2 |   4 |   8 |  16 |
# --------------------------------------------
# 2^n           |
# Time to run   |   2 |   4 |  16 | 256 |65536|
# --------------------------------------------
# n^2           |
# Time to run   |   1 |   4 |  16 |  64 | 256 |
# --------------------------------------------
# n             |
# Time to run   |   1 |   2 |   4 |   8 |  16 |
# --------------------------------------------
# log_2 n       |
# Time to run   |   1 |   2 |   3 |   4 |   5 |

# The rate at which it grows, we abbreviate it to O(f(n)); e.g.
# O(2^n), O(n^2), O(n), O(log_2 n) based on how fast this time to run grows.

#%% O(n) example
# A function that sums every number from 1 to n
# and adds them individually has to do n additions.
# If n increases by 1, we have to do 1 more addition.
# Thus this grows linearly and is O(n).

# For any n, the number of computations required is n + 1.
# i.e. operations(n) = n + 1


# If each addition took 1 second to run, this function would take n seconds to run,
# since there are n additions to do.
def sum_to(n):
    sums = 0
    for i in range(1, n + 1):
        sums += n
    return n


#%% O(1) example
# A function can also run in constant time, i.e. O(1)
# The function below also sums all numbers from 1 to n,
# but does so with only 1 multiplication, 1 addition, and 1 division.
# The number of multiplications, additions, and divisions does not
# change based on the number we want to sum until.
# If n increases by 1, the number of multiplications, additions, and
# divisions remains the same.

# For any n, the number of computations required is 3.
# i.e. operations(n) = 3


# If each operation took 1 second to run, this function will ALWAYS take 3 seconds to run,
# no matter how big n gets.
def sum_to_O1(n):
    sums = n * (n + 1) / 2
    return sums


# The lesson to observe here is that the same problem
# can be solved with different time complexities.

#%% O(n^2) example
# A function that gives all pairs of values in a list.
# e.g. inputting [0, 1] will return [(0, 0), (0, 1), (1, 0), (1, 1)]
# Given a list l of size n, we must iterate over all values twice.
# We have two for loops: outer and inner.
# Outer loop runs n times, since there are n items in the list.
# Inner loop runs n times, since there are n items in the list.
# The innermost line is thus run n*n times.
# If n increases by 1, i.e. 1 more item is added,
# the number of times the innermost line is run is n^2 + 2n + 1 times.


# If each append operation took 1 second to run, this function will take n^2 seconds to run.
def generate_pairs(l):
    pairs = []
    for i in l:
        for j in l:
            pairs.append((i, j))
    return pairs

generate_pairs([1,2,3])

#%% O(2^n) example
# A function that generates the Fibonacci sequence using recursion.
# Consider how many operations there are for each n.
# For fib(0) and fib(1), let us say there is 1 operation.
# For fib(2), we need to call fib(0), causing 1 operation, and fib(1), causing 1 operation.
# There is also an addition operation.
# In total, fib(2) takes  1 + 1 + 1 = 3 operations.
# For fib(3), we need to call fib(1), causing 1 operation, and fib(2), causing 3 operations.
# With the addition operation, fib(3) takes 1 + 3 + 1 = 5 operations.
# For fib(4): fib(2) = 3 operations, fib(3) = 5 operations.
# In total, fib(4) takes 3 + 5 + 1 = 9 operations.

# In general, the number of operations required is also expressed recursively:
# ops_fib(n) = ops_fib(n-1) + ops_fib(n-2) + 1

# Following this pattern and recapping:
# fib(0) and fib(1) take 1 operation.
# fib(2): 3 operations
# fib(3): 5 operations
# fib(4): 9 operations
# fib(5): 15 operations
# fib(6): 25 operations
# fib(7): 41 operations

# fib(25): 242,785 operations
# fib(26): 392,835 operations
# fib(27): 635,621 operations
# fib(28): 1,028,457 operations
# fib(29): 1,664,079 operations
# fib(30): 2,692,537 operations

# ...
# fib(60): 5,009,461,563,921 (5e12, or 5 trillion) operations

# The number of operations grows **exponentially** with its input.
# Importantly, this is worse than any polynomial growth rate.
# It doesn't grow exactly at O(2^n), actually at O(1.618^n).


def fib(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return fib(n - 1) + fib(n - 2)


#%% Fibonacci but efficient
# Compared to the above, the number of operations grows linearly.
# fib_On(0) and fib_On(1) take 1 operation.
# fib_On(2) has 2 assignments, and iterates through the loop once.
# In each iteration of the loop, there are 2 assignments and 1 addition, for 3 operations total.
# In total, there are 2 + 3 = 5 operations
# fib_On(3) has 2 assignments, and iterates through the loop twice.
# Each iteration of the loop has 3 operations.
# In total, there are 2 + 2*3 = 8 operations.

# In general, for any n >= 2, the number of computations is
# 2 + 3*(n-1

# Following this pattern, fib_On(60) has 2 + 59*3 = 179 operations.
# Compared with the 5 trillion operations the recursive version takes...
# this is much more efficient.


def fib_On(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else:
        f0 = 0
        f1 = 1
        for i in range(n - 1):
            f0, f1 = f1, f0 + f1
        return f1


for i in range(10):
    print(fib(i), fib_On(i))


#%% Q1a
def simple_search(listy, value):
    # Best case: the value you are searching for is the first item in the list.
    # O(1)

    # Average case: the value you are searching for is in the middle of the list.
    # To get to the middle of the list, you have to get through n/2 items.
    # O(n)

    # Worst case: the value you are searching for is at the end of the list.
    # To get to the last item in the list, you have to get through n items.
    # O(n)

    # Iterate through every item of the list
    # until we find the value of interest
    for item in listy:
        if item == value:
            return True
    return False


#%%
listy = list(range(1000))
simple_search(listy, 500)


#%% Q1b
# This version of binary search suffers from copying the list in the computers memory.
def naive_binary_search_recursive(sorted_list, value):
    # print(f"searching for {value} in {sorted_list}")
    # Best case: the value you are searching for is in the *exact middle* of the list
    # and is the *first* item we look at, no matter the size of the list.
    # O(1)

    # Worst case: *one example*: the value you are searching for is
    # the first or last item in the list, and is always the leftmost or rightmost item
    # in the part of the list we are considering.
    # Because the algorithm only checks the middle item, the only time we can check the
    # leftmost or rightmost item is when it is the only item to check, i.e. a list of 1 item.
    # How long does it take to get to a list of 1 item?
    # Each step in the binary search algorithm halves the length of the list we consider.
    # Thus, in at most log_2 n steps, we will end with a list of only 1 item.
    # O(log_2 n) = O(log n). these two are equivalent.

    # Average case: the value you are searching for is not in the exact middle
    # and is not one of the worst case positions.
    # O(log_2 n) = O(log n)

    # Base cases
    # 1. If list is empty, value was not in sorted_list
    n = len(sorted_list)
    if n == 0: return False

    # 2. If item at middle of list was value, value was in list.
    i = n // 2
    middle_item = sorted_list[i]
    if middle_item == value: return True

    # Recursive cases
    if value < middle_item:
        # if value was in sorted_list, it would be on the left.
        # thus, perform binary search on everything to the left.
        return naive_binary_search_recursive(sorted_list[:i], value)
    else:
        # value > middle_item
        # if value was in sorted_list, it would be on the right.
        # thus, perform binary search on everything to the right.
        return naive_binary_search_recursive(sorted_list[i + 1:], value)


l = list(range(20))
naive_binary_search_recursive(l, 11)

#%%
listy = list(range(1000))
naive_binary_search_recursive(listy, 600)

#%% Q1c
import time, random


def timeit(function, n, value):
    listy = list(range(n))
    start = time.time()

    # on these examples, since they use the complete list,
    # the functions should find the values.
    if not function(listy, value):
        print("function couldn't find value?")
    end = time.time()
    return end - start


for i in range(3, 9):
    n = 10**i
    value = random.randint(0, n - 1)
    print(f"searching for value {value} in {n}")
    print(
        f"simple_search on 10^{i} items took {round(timeit(simple_search, n, value),4)}s"
    )
    print(
        f"binary_search_recursive on 10^{i} items took {round(timeit(naive_binary_search_recursive, n, value),4)}s"
    )
    print()


#%% more efficient recursive function
def binary_search_recursive(sorted_list, value, left=0, right=None):
    # best/average/worst case: O(1), O(log n), O(log n), as above.

    n = len(sorted_list)

    if right is None:
        right = n - 1

    # base cases
    # if list is empty, value was not in sorted_list
    if left > right:
        return False

    # if item at middle of list was value, value was in list.
    i = (left + right) // 2
    middle_item = sorted_list[i]
    if middle_item == value: return True

    # recursive step
    if value < middle_item:
        # if value was in sorted_list, it would be on the left.
        return binary_search_recursive(sorted_list, value, left, i - 1)
    elif value > middle_item:
        # if value was in sorted_list, it would be on the right.
        return binary_search_recursive(sorted_list, value, i + 1, right)


#%%
for i in range(3, 9):
    n = 10**i
    value = random.randint(0, n - 1)
    print(f"searching for value {value} in {n}")
    print(
        f"simple_search on 10^{i} items took {round(timeit(simple_search, n, value),4)}s"
    )
    print(
        f"IMPROVED binary_search_recursive on 10^{i} items took {round(timeit(binary_search_recursive, n, value),4)}s"
    )
    print()


#%% Q3
def binary_search_iterative(sorted_list, value):
    # Same complexity as binary search above.
    l = 0
    r = len(sorted_list) - 1

    while l <= r:
        i = (r + l) // 2

        if sorted_list[i] == value:
            return True

        elif value < sorted_list[i]:
            # value belongs on the left
            r = i - 1

        elif value > sorted_list[i]:
            # value belongs on the right
            l = i + 1
    return False


#%%
listy = list(range(1000))
binary_search_iterative(listy, 600)

#%% timing testing
for i in range(3, 9):
    n = 10**i
    value = random.randint(0, n - 1)
    print(f"searching for value {value} in {n}")
    print(
        f"simple_search on 10^{i} items took {round(timeit(simple_search, n, value),4)}s"
    )
    print(
        f"binary_search_recursive on 10^{i} items took {round(timeit(binary_search_recursive, n, value),4)}s"
    )
    print(
        f"binary_search_iterative on 10^{i} items took {round(timeit(binary_search_iterative, n, value),4)}s"
    )
    print()


#%% Q2
def simple_count(sorted_list, value):
    # Given a sorted list of size n, simple_count is O(n).
    # Best case: the first value in sorted_list is larger than value.
    # We can immediately determine that the value cannot possibly exist in sorted_list.
    # O(1)

    # Average case: the value occurs in the middle of the sorted list.
    # To get to the middle of the list, we need to iterate through n/2 other items first.
    # O(n)

    # Worst case: the value occurs at the end of the sorted list.
    # To get to the end of the list, we need to iterate through n other items first.
    # O(n)

    count = 0

    # if empty list
    if len(sorted_list) == 0: return 0

    # iterate through every item in the list
    for item in sorted_list:
        if item > value:
            # if we are at an item which is larger than the value we want to count,
            # there cannot possibly be any more occurrences of value in the list.
            break
        elif item == value:
            # found an occurrence of value.
            count += 1

    return count


#%% Q2 - with at most 10 occurrences
def binary_search_index(sorted_list, value):
    # Perform binary search, but return the index at which the value occurs.
    # May have more occurrences of value to the left and right.
    l = 0
    r = len(sorted_list) - 1

    while l <= r:
        i = (r + l) // 2

        if sorted_list[i] == value:
            return i

        elif value < sorted_list[i]:
            # value belongs on the left
            r = i - 1

        elif value > sorted_list[i]:
            # value belongs on the right
            l = i + 1

    # value not found.
    return -1


def binary_count_simple(sorted_list, value):
    # Best case: the value we are searching for is in the *exact middle* of the list.
    # Binary search takes O(1) time.
    # There are at most 10 occurrences of the value.
    # It takes at most 10 comparisons to count them.
    # Counting takes O(1) time.
    # In total this takes O(1) + O(1) = O(1) time.

    # Worst case: *one example*: the value we are searching for is at the very start of the list.
    # As per previous explanation, binary search takes O(log_2 n) = O(log n) time.
    # There are at most 10 occurrences of the value.
    # It takes at most 10 comparisons to count them.
    # Counting takes O(1) time.
    # In total this takes O(log n) + O(1) = O(log n) time.

    # Average case: the value we are searching for is not in the middle.
    # As per previous explanation, binary search takes O(log n) time.
    # There are at most 10 occurrences of the value.
    # It takes at most 10 comparisons to count them.
    # Counting takes O(1) time.
    # In total this takes O(log n) + O(1) = O(log n) time.

    # Find the index at which value occurs in the sorted list
    i = binary_search_index(sorted_list, value)

    # if not found, no occurrences.
    if i == -1: return 0

    # if found in list, count occurrences.
    n = len(sorted_list)
    count = 1
    start = i - 1
    end = i + 1
    # search to the left of where we found the value
    while sorted_list[start] == value:
        start -= 1
        count += 1
        if start == -1: break
    # search to the right of where we found the value
    while sorted_list[end] == value:
        end += 1
        count += 1
        if end == n: break
    return count


listy = [1, 2, 2, 4, 4, 4, 4, 5, 6, 6, 6]
print(listy)
for i in range(8):
    print(binary_count_simple(listy, i), "occurrences of", i)

# This is problematic if there is no cap on the number of occurrences of value in the list.
# If the list consisted of n copies of the same number, then we immediately find the value,
# but take O(n) time to count them:
# Counting the occurrences on the the left takes n/2 comparisons and is O(n)
# Counting the occurrences on the the right takes n/2 comparisons and is O(n)
# Thus if the list is n copies of the same number, then the time complexity is:
# O(1) + O(n) + O(n) = O(n)
# where O(1) is the time it takes to find the index using binary search
# and the two O(n) terms are for counting to the left and to the right.


#%% Q2 - no maximum number of occurrences
# The below will only terminate once it's narrowed down to a *single* index.
# This compares to the above, where it stopped once it found a value of interest.
def binary_search_left(sorted_list, value):
    """
    Searches for the leftmost occurrence of value
    (if it exists in sorted_list)
    """
    l = 0
    r = len(sorted_list) - 1
    while l <= r:
        i = (l + r) // 2
        if value == sorted_list[i]:
            # want to find the leftmost occurrence, so go left.
            r = i - 1
        elif value < sorted_list[i]:
            # value belongs to the left
            r = i - 1
        elif value > sorted_list[i]:
            # value belongs to the right
            l = i + 1
    return l  # return l, which is always the index of interest.


def binary_search_right(sorted_list, value):
    l = 0
    r = len(sorted_list) - 1
    while l <= r:
        i = (l + r) // 2
        if value == sorted_list[i]:
            l = i + 1
        elif value < sorted_list[i]:
            # value belongs to the left
            r = i - 1
        else:
            # value > sorted_list[i]
            # value belongs to the right
            l = i + 1
    return l


def binary_count_binary_search(sorted_list, value):
    l_i = binary_search_left(sorted_list, value)
    r_i = binary_search_right(sorted_list, value)
    if r_i == l_i:
        if r_i > len(sorted_list) - 1: return 0
        if sorted_list[r_i] == value: return 1
    return r_i - l_i


listy = [1, 2, 2, 4, 4, 4, 5, 6, 6, 6]
print(listy)
for i in range(8):
    print(binary_count_binary_search(listy, i), "occurrences of", i)

#%% Q2 testing
for i in range(3, 6):
    n = 10**i
    max_n = 10**(i - 2)

    listy = []
    for _ in range(n):
        listy.append(random.randint(0, max_n))

    listy.sort()

    for j in range(max_n):
        simple_count_result = binary_count_simple(listy, j)
        binary_count_result = binary_count_binary_search(listy, j)
        if simple_count_result != binary_count_result:
            print(
                f"mismatch in results! counting {j}, {simple_count_result} vs {binary_count_result}"
            )
            break
        if i < 6:
            print(f"there were {binary_count_result} occurrences of value {j}")
    print()


#%% Q4
def index_equal_value(sorted_list):
    # Functionally the same as binary search, just with a different value we are searching for.
    l = 0
    r = len(sorted_list) - 1

    while l <= r:  # same terminating condition
        i = (r + l) // 2
        # the value we are looking for is always the index we are at.
        val = i

        # base case - what we were looking for
        if val == sorted_list[i]:
            return i

        elif val < sorted_list[i]:
            # the value we are looking for would be on the left.
            r = i - 1

        else:  # val > sorted_list[i]
            # the value we are looking for would be on the right.
            l = i + 1
    return False


#%% alternative way to think about it, effectively equivalent
# Instead of thinking about the value changing, we can think about
# changing the list.
# If we take all entries in the list and subtract the index,
# forming a new (fixed) list,
# then we want to find an entry equal to 0.
random.seed(888)
random_list = random.sample(range(-20, 20), 10)
random_list.sort()
random_list_transformed = [random_list[i] - i for i in range(len(random_list))]
# However, this changing of the list takes O(n) time
# where n is the number of entries in the list.
# negating all gains from using binary search with O(log n) time.
print(random_list)
print(random_list_transformed)

print(binary_search_iterative(random_list_transformed, 0))


#%%
# The only changes compared to the previous version are
# the shifting of the variable val/i to the right side of the inequality
# no need to change the entire list, instead only when we need it.
def index_equal_value_alt(sorted_list):
    l = 0
    r = len(sorted_list) - 1

    while l <= r:  # same terminating condition
        i = (r + l) // 2

        # base case - what we were looking for
        if 0 == sorted_list[i] - i:
            return i

        elif 0 < sorted_list[i] - i:
            # the value we are looking for would be on the left.
            r = i - 1

        else:  # 0 > sorted_list[i] - i
            # the value we are looking for would be on the right.
            l = i + 1
    return False


#%% guaranteed to give me the correct answer
def simple_index_equal_value(sorted_list):
    if len(sorted_list) == 0: return

    for i, val in enumerate(sorted_list):
        if i == val:
            return i
        if val > i:
            # cannot increase index fast enough
            return False


#%%
import random

listy = []
n = 10000
for i in range(n):
    rv = random.sample(range(-n // 2, 2 * n), n)
    listy.append(rv)
listy.sort()

print(simple_index_equal_value(listy))
print(index_equal_value(listy))
