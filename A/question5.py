# Linear Search

import timeit

start = timeit.default_timer()


def binary_search(array, ele):
    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if array[mid] == ele:
            found = True
        else:
            if ele < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


array = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("The item is in array: ", binary_search(array, 13))
print("The item is in array: ", binary_search(array, 12))

end = timeit.default_timer()
print("The time required to found is: ", end-start, " second")