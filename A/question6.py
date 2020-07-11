# Linear Search

import timeit

start = timeit.default_timer()


def linear_search(array, ele):
    pos = 0
    found = False
    stop = False

    while pos<len(array) and not found and not stop:
        if array[pos] == ele:
            found = True
        else:
            if array[pos]>ele:
                stop = True
            else:
                pos += 1
    return found

array = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("The item in array: ", linear_search(array, 13))
print("The item in array: ", linear_search(array, 13))



end = timeit.default_timer()

print("The time required to find an item is: ", end-start, " second")