from priority_queue_base_class import PriorityQueueBase


class HeapPQ(PriorityQueueBase):

    @staticmethod
    def parent(j):
        """ Return the position of the parent node of j """

        return (j - 1) // 2

    @staticmethod
    def left(j):
        """ Return the position of the left child """
        return 2 * j + 1

    @staticmethod
    def right(j):
        """ Return the position of the right child """
        return 2 * j + 2

    def __init__(self):
        self._data = []

    def min(self):
        self.assert_not_empty()
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """ Removes the item with the minimum key """
        self.assert_not_empty()
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        item = self._data.pop()
        self.downheap_bubble(0)
        return (item._key, item._value)

    def has_right(self, j):
        """ Returns True if position j has a right child """
        right = self.right(j)
        return right < len(self)

    def has_left(self, j):
        """ Returns True if position j has  left child """

        left = self.left(j)
        return left < len(self)

    def downheap_bubble(self, p):
        """ Downheap bubble the item at position p """

        if self.has_left(p):

            left = self.left(p)
            smaller = left
            if self.has_right(p):
                right = self.right(p)

                if self._data[right] < self._data[left]:
                    smaller = right

            if self._data[smaller] < self._data[p]:
                self._data[smaller], self._data[p] = self._data[p], self._data[smaller]
                self.downheap_bubble(smaller)

    def upheap_bubble(self, q):
        """ Upheap bubble the item at position q """
        p = self.parent(q)
        if q > 0 and self._data[q] < self._data[p]:
            # swap
            self._data[p], self._data[q] = self._data[q], self._data[p]
            self.upheap_bubble(p)

    def add(self, k, v):
        # 1. append
        # 2. upheap bubble
        item = self._Item(k, v)
        self._data.append(item)
        self.upheap_bubble(len(self) - 1)

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    pq = HeapPQ()

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
