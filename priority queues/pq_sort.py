from unsorted_list_priority_queue import UnsortedListPQ
from doubly_linked_positional_list import PositionalList

L = PositionalList()
L.add_last(4)
L.add_last(3)
L.add_last(0)
L.add_last(-1)
L.add_last(10)
L.add_last(8)


def pq_sort(L):
    """ L: positional List """

    n = len(L)
    heapq = UnsortedListPQ()
    for _ in range(n):
        v = L.delete(L.first())
        heapq.add(v, v)

    # sort
    for i in range(n):
        _, v = heapq.remove_min()
        L.add_last(v)


pq_sort(L)
for v in L:
    print(v)

