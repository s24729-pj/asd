import sys
from random import randint
from time import time


def partition(array, p, r):
    pivot = array[r]
    smaller = p

    for j in range(p, r):
        if array[j] <= pivot:
            array[smaller], array[j] = array[j], array[smaller]
            smaller = smaller + 1

    array[smaller], array[r] = array[r], array[smaller]
    return smaller


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


# Zniesienie limitu rekursji
# sys.setrecursionlimit(300000)

numbers = []

for i in range(300000):
    numbers.append(randint(0, 9))

n = len(numbers)

quicksort_start = time()
quicksort(numbers, 0, n - 1)
quicksort_end = time()
quick_sort_duration = quicksort_end - quicksort_start

print("Czas trwania quicksort:")
print(quick_sort_duration)

# print("Posortowana tablica:")
# for number in numbers:
#     print("%d " % number, end='')
