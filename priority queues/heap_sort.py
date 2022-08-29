# Phase 1. Max-Heap construction
def downheap_bubble(array, N, j):
    """
        build a max-heap
        array: [...]
        N: 0 to N - 1 elements of array are considered part of the hip
        j: the index to downheap bubble

    """
    has_left = lambda i: 2 * i + 1 < N
    has_right = lambda i: 2 * i + 2 < N

    if has_left(j):
        left = 2 * j + 1
        large = left

        if has_right(j):
            right = 2 * j + 2
            if array[right] > array[left]:
                large = right

        # swap
        if array[large] > array[j]:
            array[large], array[j] = array[j], array[large]
            downheap_bubble(array, N, large)


def heapify(array):
    """
        build a max-heap
        array: [...]
    """

    start = len(array) // 2 - 1

    for i in range(start, -1, -1):
        downheap_bubble(array, len(array), i)


arr = [25, -2, -10, 5, 1, 8, 10, -1, 0, 15, 20, 35, 2]

heapify(arr)
print(arr)
# Phase 2. Heap Sort
for i in range(len(arr) - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    downheap_bubble(arr, i, 0)


print(arr)
