class Empty(Exception):
    pass


class LinkedQueue:

    class _Node:
        __slots__ = "_elem", "_next"

        def __init__(self, elem, next):
            self._elem = elem
            self._next = next

    def __init__(self):
        self._head = None
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
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    def dequeue(self):
        self.assert_not_empty()
        result = self._head._elem
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

    def first(self):
        self.assert_not_empty()
        return self._head._elem