# Interpolation Search


def interpolation_search(arr, low, high, x):

    if (low <= high and x >= arr[low] and x <= arr[high]):
        pos = low + ((high - low) // (arr[high] - arr[low]) *
                    (x - arr[low]))
        # Condition of target found
        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, high, x)

        if arr[pos] > x:
            return interpolation_search(arr, low, pos - 1, x)
    return -1


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

x = 33
index = interpolation_search(arr, 0, n - 1, x)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

