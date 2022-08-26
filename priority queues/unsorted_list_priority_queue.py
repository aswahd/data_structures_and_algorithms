from priority_queue_base_class import PriorityQueueBase
from doubly_linked_positional_list import PositionalList


class Empty(Exception):
    pass


class UnsortedListPQ(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def find_min(self):
        """ Returns the position of the item with the minimum key """
        self.assert_not_empty()
        _min = self._data.first()
        walk = self._data.after(_min)

        while walk is not None:
            if walk.element() < _min.element():
                _min = walk

            walk = self._data.after(walk)

        return _min

    def min(self):
        """ Return the key and value of the item with the minimum key """
        item = self.find_min().element()
        return (item._key, item._value)

    def remove_min(self):
        """" """
        item = self._data.delete(self.find_min())
        return (item._key, item._value)

    def add(self, k, v):
        self._data.add_last(self._Item(k, v))

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    pq = UnsortedListPQ()

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
