from binary_heap_array import HeapPQ

heapq = HeapPQ()

heapq._data = [HeapPQ._Item(10, 5),
               HeapPQ._Item(2, -1),
               HeapPQ._Item(8, 3),
               HeapPQ._Item(1, 2),
               HeapPQ._Item(3, 5),
               HeapPQ._Item(18, 0),
               HeapPQ._Item(0, 9),
               ]


def heapify(D):
    """ Bottom up heap construction """
    start = D.parent(len(D) - 1)

    for i in range(start, -1, -1):
        D.downheap_bubble(i)


heapify(heapq)
print(heapq.remove_min())
print(heapq.remove_min())
print(heapq.remove_min())
print(heapq.remove_min())
print(heapq.remove_min())
print(heapq.remove_min())
print(heapq.remove_min())
