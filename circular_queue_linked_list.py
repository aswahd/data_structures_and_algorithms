class Empty(Exception):
    pass


class CircularQueue:
    class _Node:
        __slots__ = "_elem", "_next"

        def __init__(self, elem, next):
            self._elem = elem
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def assert_not_empty(self):
        if self.is_empty():
            raise Empty('Empty Queue!')

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1

    def dequeue(self):
        self.assert_not_empty()
        result = self._tail._next._elem
        self._tail._next = self._tail._next._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

    def first(self):
        self.assert_not_empty()
        return self._tail._next._elem

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


D = CircularQueue()
D.enqueue(5)
D.enqueue(4)
D.enqueue(2)

for i in range(9):
    el = D.first()
    print(el)
    D.rotate()