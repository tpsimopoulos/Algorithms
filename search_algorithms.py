# Iterative Binary Search #

def binarysearch(arr, n):
    first = 0
    last = len(arr) - 1
    found = False

    while not found:

        middle = (first + last) // 2

        if arr[middle] == n:
            return middle
        elif arr[middle] > n:
            last = middle - 1
        else:
            first = middle + 1

binarysearch([1,2,3,4,5,6,7], 7)


# Recursive Binary Search #

def binarysearch_recursive(arr, n, first=0, last=None):

    if last == None:
        last = len(arr)-1

    middle = (first + last) // 2

    if arr[middle] == n:
        return middle
    elif arr[middle] > n:
        return binarysearch_recursive(arr, n, last=middle-1)
    else:
        return binarysearch_recursive(arr, n, first=middle+1)

binarysearch_recursive([1,2,3,4,5,6,7], 7)
