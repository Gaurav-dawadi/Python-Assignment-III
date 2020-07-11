# Quick Sort

import timeit
from random import randint

start = timeit.default_timer()


def quickSort(array):

    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array)-1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        else:
            same.append(item)

    return quickSort(low) + same + quickSort(high)


print("The sorted array is: ", quickSort([8, 2, 6, 4, 5]))
end = timeit.default_timer()
print("Time taken to sort array is: ", end-start, " seconds")