# Selection Sort #

def findMax(arr):
    largest_val = 0
    largest_index = 0
    for i in range(len(arr)):
        if arr[i] > largest_val:
            largest_index = i

    return largest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(findMax(arr))) # pops the highest value's index off arr
    return new_arr

selection_sort([1,2,3,4,5,6,7])


# Quicksort #

def quicksort(arr):

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

quicksort([1,23,34,5,23,523,234234,2])
