import sys
from random import randint
from time import time


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, i):
    l = left(i)
    r = right(i)
    heap_size = len(A)

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    heap_size = len(A)

    for i in range(((heap_size - 1) // 2), 0, -1):
        max_heapify(A, i)


def heapsort(A):
    build_max_heap(A)
    heap_size = len(A)

    for i in range(heap_size - 1, 1, -1):
        A[i], A[0] = A[0], A[i]
        heap_size = heap_size - 1
        max_heapify(A, 0)


# Zniesienie limitu rekursji
# sys.setrecursionlimit(300000)

numbers = []

for i in range(300000):
    numbers.append(randint(0, 9))

n = len(numbers)

heapsort_start = time()
heapsort(numbers)
heapsort_end = time()
heap_sort_duration = heapsort_end - heapsort_start

print("Czas trwania heapsort:")
print(heap_sort_duration)

# print("Posortowana tablica:")
# for number in numbers:
#     print("%d " % number, end='')
