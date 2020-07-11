# Bubble Sort Algorithm
import timeit

start = timeit.default_timer()

def bubbleSort(array): 
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array
     
print("The sorted array is ", bubbleSort([8, 2, 6, 4, 5]))

end = timeit.default_timer()

print("The total time required: ", end-start, " seconds")