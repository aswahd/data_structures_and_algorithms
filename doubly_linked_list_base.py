class Empty(Exception):
    pass


class DoublyLinkedListBase:

    class _Node:

        __slots__ = "_elem", "_prev", "_next"

        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, self._header, None)
        self._header._next = self._trailer
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def assert_not_empty(self):
        if self.is_empty():
            raise Empty('Empty List!')

    def insert_between(self, e, predecessor, successor):
        node = self._Node(e, predecessor, successor)
        predecessor._next = node
        successor._prev = node
        self._size += 1
        return node

    def delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        result = node._elem
        node._prev = node._next = node._elem = None  # deprecated node
        self._size -= 1
        return result

