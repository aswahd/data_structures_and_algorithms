import sys
sys.path.append('.')
from doubly_linked_positional_list import PositionalList    
from binary_heap_array import HeapPQ


# Create unsorted positional list
array = PositionalList()
array.add_last(10)
array.add_last(0)
array.add_last(3)
array.add_last(-1)
array.add_last(50)
array.add_last(20)


def pq_sort(L):
    """ L: positional list """

    pq = HeapPQ()

    for i in range(len(L)):
        v = L.delete(L.first())

        pq.add(v, v)
    
    # sort
    for i in range(len(pq)):
        _, v = pq.remove_min()
        L.add_last(v)
    

pq_sort(array)

for v in array:
    print(v)


