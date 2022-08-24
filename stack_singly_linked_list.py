class Empty(Exception):
    pass


class LinkedStack:

    class _Node:
        __slots__ = "_elem", "_next"

        def __init__(self, elem=None, next=None):
            self._elem = elem
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        self.assert_not_empty()
        result = self._head._elem
        self._head = self._head._next
        self._size -= 1
        return result

    def top(self):
        self.assert_not_empty()
        return self._head._elem

    def assert_not_empty(self):
        if self.is_empty():
            raise Empty('Empty Stack!')
