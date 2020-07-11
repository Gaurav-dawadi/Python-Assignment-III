# Tower of Hanoi

count = 0
A = [1, 2, 3, 4, 5]
B = []
C = []


def tower_of_hanoi(A, B, C, n):
    global count

    if n == 1:
        C.append(A.pop())
        count += 1
    else:
        tower_of_hanoi(A, C, B, n-1)
        tower_of_hanoi(A, B, C, 1)
        tower_of_hanoi(B, A, C, n-1)
    return A, B, C, count


tower_of_hanoi(A, B, C, 5)
print(A)
print(B)
print(C)
print(count)
