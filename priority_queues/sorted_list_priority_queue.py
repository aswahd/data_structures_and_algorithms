import sys
sys.path.append('.')

from priority_queue_base_class import PriorityQueueBase
from doubly_linked_positional_list import PositionalList


class SortedListPQ(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def min(self):
        self.assert_not_empty()
        item = self._data.first().element()
        return (item._key, item._value)

    def remove_min(self):
        self.assert_not_empty()
        item = self._data.delete(self._data.first())

        return (item._key, item._value)

    def add(self, k, v):
        item = self._Item(k, v)
        walk = self._data.first()
        while walk is not None and item > walk.element():
            walk = self._data.after(walk)
        if walk is None:
            self._data.add_last(item)
        else:
            self._data.add_before(walk, item)

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    pq = SortedListPQ()

    pq.add(5, 'A')
    pq.add(9, 'C')
    pq.add(3, 'B')
    pq.add(7, 'D')
    print(pq.min())
    print(pq.remove_min())
    print(pq.remove_min())
    print(len(pq))
    print(pq.remove_min())
    print(pq.remove_min())
    print(pq.is_empty())
    print(pq.remove_min())
