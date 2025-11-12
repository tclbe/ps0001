#%% Q1
listy = ['Foxtrot', 'Bravo', 'Echo', 'Delta', 'Charlie', 'Alfa']
help(sorted)

#%%
# sorted() returns a new list
# and so does not modify the original input.
print("listy:", listy)
print("sorted:", sorted(listy))
print("listy:", listy)


#%% Q1a
def comp_second(string):
    if len(string) == 0: return ""
    return string[1:]

#%%
# specifying the key will sort the list according
# to the values after the function is applied.
# for example, the below key will sort the list
# based on these values:
print(listy)
print("The list will be sorted according to:")
print([comp_second(x) for x in listy])

#%%
print(sorted(listy, key=comp_second))

#%% Q1a - lambda function (anonymous function)
# out of syllabus
# used for extremely short functions.
print(sorted(listy, key=lambda s: s[1:]))

#%% Q1a - lambda function, taking care of empty strings.
# equivalent to comp_second answer above
print(sorted(listy, key=lambda s: s[1:] if len(s) > 0 else ""))

#%% Q1b
def comp_len(string):
    return len(string)
print(listy)
print([comp_len(x) for x in listy])

#%%
print(sorted(listy, key=comp_len))

#%% Q1b - equivalent
print(sorted(listy, key=len))

#%% Q2 setup
listy = [3, 6, 2, 5, 1, 4, 3]

print(sorted(listy))

#%% Q2
def insertion_sort(in_l):
    # If in_l is length 0 or 1, it is sorted.
    if len(in_l) <= 1: return in_l
    
    sorted_l = []
    
    # Cycle over every item in in_l
    for to_insert in in_l:
        # This is the index in sorted_l where to_insert
        # should be inserted.
        # We will update it based on the entries of
        # sorted_l
        insert_index = 0
        
        # Starting from the smallest item in sorted_l
        # (index 0) and increasing, find the item in
        # sorted_l which is just bigger than to_insert.
        # to_insert will belong just before it.
        for j in range(len(sorted_l)):
            if sorted_l[j] > to_insert:
                insert_index = j
                break
        else:
            # The end was reached - to_insert is the largest
            # in sorted_l and belongs at the end.
            sorted_l.append(to_insert)
            
            # track the status of sorting
            # print(sorted_l)
            
            # Go to next item.
            continue
            
        # Insert to_insert where we determined
        # the next item is bigger than to_insert.
        sorted_l.insert(insert_index, to_insert)
        
        # track the status of sorting
        # print(sorted_l)
    return sorted_l

print(insertion_sort(listy))

#%% Q2 pdf solution
def insertion_sort(inlist):
    """ Implements the insertion sort algorithm
    takes as input a ( possibly ) unsorted list
    and outputs the corresponding sorted list """
    outlist = [inlist [0]]
    # for all the elements in the input list
    for j in range (1, len(inlist)):
        # identify where this element needs to be placed
        # in the current sorted output list
        i = 0
        while outlist [i] < inlist[j]:
            i += 1
            # go out of the loop in case you reached the end of the list
            if i == len(outlist):
                break
        outlist.insert(i, inlist[j])
        
    return outlist

listy = list(range(7,0,-1))
print(listy)
insertion_sort(listy)

#%% Q3
def selection_sort(in_l):
    # Make a copy since algorithm below mutates the input list.
    in_l = in_l.copy()
    
    # If in_l is length 0 or 1, it is sorted.
    if len(in_l) <= 1: return in_l

    sorted_l = []
    
    # 
    for i in range(len(in_l)):
        smallest_index = i
        for j in range(i, len(in_l)):
            if in_l[j] < in_l[smallest_index]:
                smallest_index = j
                
        # Add the smallest element to sorted_l
        sorted_l.append(in_l[smallest_index])
        
        # Swap the smallest element to the front.
        in_l[i], in_l[smallest_index] = in_l[smallest_index], in_l[i]
        
        # track the status of sorting
        print("sorted_l:", sorted_l)
        
        # track the swapping
        print(f"swapped index {i} and {smallest_index}: {in_l}")

    return sorted_l

print([3,6,2,1])
print(selection_sort([3,6,2,1]))

#%% Q3 pdf solution
def selection_sort(inlist):
    """ Implements the selection sort algorithm
    takes as input a ( possibly ) unsorted list
    and outputs the corresponding sorted list """
    outlist = []
    # for all the elements in the input list
    while len(inlist) > 0:
        # identify the minimum element of inlist
        my_min = inlist[0]
        my_min_index = 0
        for i in range(1, len(inlist)):
            if inlist[i] < my_min:
                my_min = inlist[i]
                my_min_index = i
            # append this minimum element in outlist
            # and remove it from inlist
        outlist.append(inlist[my_min_index])
        del inlist [my_min_index]
    return outlist

listy = list(range(7,0,-1))
print(listy)
selection_sort(listy)

#%% Q4
listy = list(range(7,0,-1))
def merge_sort_iter(in_l, debug=False):
    n = len(in_l)

    # If in_l is length 0 or 1, it is sorted.
    if n <= 1: return in_l
    
    in_l = in_l.copy()

    # Start with 1-element sublists, to be sorted into 2-element sublists.
    sort_size = 1
    
    # Sort until sort_size is at least the list size.
    while sort_size <= n:
        if debug:
            print("\tsort_size:", sort_size)
            
        # Given sort_size, the number of 2*sort_size sublists is:
        # length of list // 2 * sort_size + 1
        for i in range(n // (2*sort_size) + 1):
            # This is the start and end index
            # of the 2*sort_size sublist to be sorted.
            start_i = i * 2*sort_size
            end_i = min(start_i + 2*sort_size, n)

            # We must get the start indexes of the left and right lists,
            # and the end indexes of the left and right lists.
            # min() is used to prevent indexing past the end.
            # Why is it start_i + sort_size?
            # Because we are interested in sorting the slices of size sort_size.
            # Make sure you understand why the indexes are as below.
            left_l_start = start_i
            left_l_end = min(start_i + sort_size, n)
            right_l_start = min(start_i + sort_size, n)
            right_l_end = min(start_i + 2*sort_size, n)
            
            left_l = in_l[left_l_start: left_l_end]
            right_l = in_l[right_l_start:right_l_end]

            if debug:
                print("sorting slices", left_l, right_l)

            # merge the lists to sort
            # exactly the same merge algorithm in recursive mergesort
            result_l = []
            while left_l and right_l:
                if left_l[0] < right_l[0]:
                    result_l.append(left_l.pop(0))
                else:
                    result_l.append(right_l.pop(0))
            if left_l:
                result_l.extend(left_l)
            elif right_l:
                result_l.extend(right_l)
                
            # After merging, the slice is sorted.
            if debug:
                print("slice sorted", result_l)
            # Replace the unsorted slice with the sorted slice.                
            in_l[start_i:end_i] = result_l
        
        if debug:
            print(f"sort size {sort_size} done, list: {in_l}")
        # Run out of slices of size sort_size, increase.
        sort_size *= 2
    
    return in_l

print(listy)
merge_sort_iter(listy, True)

#%% Q4 pdf solution
def merge_sort_iterative(inlist):
    """ Implement the merge sort algorithm without
    using recursive function (aka iterative implementation)
    Takes as input a (possibly) unsorted list
    and outputs the corresponding sorted list """
    outlist = inlist[:]
    # we will test successive powers of two for sublist sizes
    # aka we start from 1, then 2, then 4, then 8, etc.
    # and we continue until the sublist size is bigger than the list itself
    sub_list_size = 1
    while sub_list_size < len(inlist):
    # we will test all adjacent sublists of size sub_list_size
    # and merge them together while keeping the property that they are sorted
        for start_index in range(0, len(inlist), 2*sub_list_size):
            # we extract the two adjacent sublists ( left and right )
            left_list = outlist[start_index : start_index+sub_list_size]
            right_list = outlist [ start_index + sub_list_size : start_index + 2*sub_list_size]
            # we merge these two lists together
            # while keeping the property that everythin is property
            my_sorted_list = []
            while left_list != [] or right_list != []:
                if left_list == []:
                    my_sorted_list.append(right_list.pop(0))
                elif right_list == []:
                    my_sorted_list.append(left_list.pop(0))
                elif left_list[0] < right_list[0]:
                    my_sorted_list.append(left_list.pop(0))
                else :
                    my_sorted_list.append(right_list.pop(0))
            outlist[start_index : start_index+ 2*sub_list_size] = my_sorted_list[:2*sub_list_size]
        sub_list_size *= 2
    return outlist

listy = list(range(7,0,-1))
print(listy)
merge_sort_iterative(listy)
