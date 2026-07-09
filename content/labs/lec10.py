def bubblesort(l):
    n = len(l)
    
    # iterate over the list at most how many items there are
    for _ in range(n):
        swapped = False
        
        # iterate over every adjacent pair of items
        # represented as indexes i and i+1
        # make sure to get only indexes until length - 1
        for i in range(n - 1):
            item1, item2 = l[i], l[i+1]
            
            # if the items are in the correct order, there is nothing to do.
            # if the items are incorrectly ordered, swap them.
            if item1 > item2:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True
                print(l)
        # if no swaps occurred, then the list is sorted.            
        if not swapped:
            return

l = [3, 1, 4, 1, 5]
print(l)
bubblesort(l)
print(l)
            
#%%
def mergesort(l):
    # The output of this function is a sorted list.
    n = len(l)
    
    # base case
    # if there are 0 or 1 elements, it is sorted.
    if n <= 1:
        return l
    else:
        # there are 2 or more items.
        left = l[:n//2]
        right = l[n//2:]
        
        # Since the output of mergesort() is sorted,
        # left and right are both sorted lists.
        left = mergesort(left)
        right = mergesort(right)
        
        # To merge the two sorted lists, we look at the smallest items in each list
        result = []
        while left and right:
            # While there are items in both left and right list
            if left[0] < right[0]:
                # The item in the left list is smaller.
                result.append(left[0])
                left.pop(0)
            else:
                # The item in the right list is smaller (or equal to) the item in the left list..
                result.append(right[0])
                right.pop(0)
        
        # One of the lists is now empty.
        # Any elements left in the non-empty list must have been larger
        # than all elements in the now empty list.
        if left:
            # Right list is empty, so all items in left list are larger
            # and are sorted.
            result.extend(left)
        elif right:
            # Left list is empty, so all items in right list are larger
            # and are sorted.
            result.extend(right)
        return result

l = [3, 1, 4, 1, 5]
print(l)
l = mergesort(l)
print(l)

#%%
def mergesort(l, depth=0, debug=False):
    n = len(l)
    
    if n <= 1:
        return l

    else:
        left = l[:n//2]
        right = l[n//2:]
        
        if debug:
            print(f"{depth:>{depth+1}} START sort left list: {left}")
        left = mergesort(left, depth+1, debug)
        if debug:
            print(f"{depth:>{depth+1}} END sort left list: {left}")
            print(f"{depth:>{depth+1}} START sort right list: {right}")
        right = mergesort(right, depth+1, debug)
        if debug:
            print(f"{depth:>{depth+1}} END sort right list: {right}")
            print(f"{depth:>{depth+1}} MERGING lists {left} and {right}")

        result = []

        while left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        
        if left:
            result.extend(left)
        elif right:
            result.extend(right)
        return result

l = [3, 4, 1, 7, 6, 2, 5]
print(l)
print(mergesort(l, 0, True))
pass
