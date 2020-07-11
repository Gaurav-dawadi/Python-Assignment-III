# insertion sort

import timeit

start = timeit.default_timer()


def insertionSort(array):

    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array 


print(insertionSort([8, 2, 6, 4, 5]))

end = timeit.default_timer()

print("The time required to sort array is: ", end-start, " seconds")