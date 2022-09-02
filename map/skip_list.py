import random
from map_base_class import MapBase


class SkipList(MapBase):

    class Item:
        __slots__ = "key", "value"

        def __init__(self, key, value):
            self.key = key
            self.value = value

    class Node:

        __slots__ = "_element", "_prev", "_next", "_below", "_above"

        def __init__(self, prev=None, next=None, below=None, above=None, element=None):
            self._element = element
            self._prev = prev
            self._next = next
            self._below = below
            self._above = above

    class Position:

        def __init__(self, node, container):
            self._node = node
            self._container = container

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return self._node is other._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        """ Return the node at position p. """
        if not isinstance(p, self.Position):
            raise TypeError("p is not a valid position type. ")

        if p._container is not self:
            raise TypeError("p is not part of this list. ")

        if p._node._next is p._node:  # convention for a deleted node.
            raise TypeError("deprecated position. ")

        return p._node

    def make_position(self, node):
        if node is None:
            return None
        return self.Position(node, self)

    def next(self, p):
        """ Return the position of the item after position p. """
        node = self._validate(p)
        return self.make_position(node._next)

    def prev(self, p):
        """ Return the position of the item before position p. """
        node = self._validate(p)
        return self.make_position(node._prev)

    def above(self, p):
        """ Return the position of the item above position p. """
        node = self._validate(p)
        return self.make_position(node._above)

    def below(self, p):
        """ Return the position of the item below position p. """
        node = self._validate(p)
        return self.make_position(node._below)

    def first(self):
        """ Returns the position of the first item in the first level of the list. """
        return self.make_position(self.header)

    def insert_after_above(self, p, q, e):
        """
            Insert (k, v) after position p, and above position q.
        """
        if p is None:
            # Create a sentinel node
            if q is not None:
                q = self._validate(q)
            new = self.Node(None, None, q, None, e)
            if q is not None :
                q._above = new
            return self.make_position(new)

        p_node = self._validate(p)
        if q is not None:
            q_node = self._validate(q)
        else:
            q_node = None

        new = self.Node(p_node, p_node._next, q_node, None, e)
        if new._next is not None:
            p_node._next._prev = new
        p_node._next = new
        if q_node is not None:
            q_node._above = new
        return self.make_position(new)

    def __init__(self):
        self.height = 0  # the height of the skip list
        self.size = 0  # the size of the list

        # Add sentinel keys
        self.start = self.header = self.insert_after_above(None, None, self.Item(float('-inf'), None))
        self.insert_after_above(self.start, None, self.Item(float('inf'), None))

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        """ Return the value of an item with key k """
        p = self.search(key)
        if p.element().key != key:
            raise KeyError("Key Error: " + repr(key))

        return p.element().value

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __iter__(self):
        """ Return an iterator of keys. """

        walk = self.next(self.header)
        for i in range(len(self)):
            yield walk.element().key
            walk = self.next(walk)

    def __delitem__(self, key):
        self.delete(key)

    def search(self, key):
        """ Return the position of the item with a key less than or equal to k or None if such a
        key doesn't exist. """

        p = self.start
        # down scanning
        while self.below(p) is not None:
            p = self.below(p)
            # forward scanning
            while key >= self.next(p).element().key:
                p = self.next(p)

        return p

    def insert(self, key, value):
        """ Insert (k, v) at an appropriate position of a sorted map. """
        p = self.search(key)
        if p.element().key == key:
            # overwrite the value
            p.element().value = value

        # Insert (k, v) after p
        q = None
        i = -1
        while True:
            i += 1
            if i >= self.height:
                self.height += 1
                # add a new level
                tail = self.next(self.start)
                self.start = self.insert_after_above(None, self.start, self.Item(-float('inf'), None))
                self.insert_after_above(self.start, tail, self.Item(float('inf'), None))

            q = self.insert_after_above(p, q, self.Item(key, value))
            while self.above(p) is None:
                p = self.prev(p)
            p = self.above(p)
            if not random.randrange(2):
                break
        self.size += 1

    def _delete(self, p):
        """ Delete position p. """
        node = self._validate(p)
        node._prev._next = node._next
        node._next._prev = node._prev
        node._below = node._above = node._prev = node._element = None
        node._next = node  # Deprecated Node

    def delete(self, key):
        """ Delete the item with key k. """
        p = self.search(key)
        if p.element().key != key:
            raise KeyError("Key Error: " + repr(key))

        while p is not None:
            above = self.above(p)
            self._delete(p)
            p = above
        self.size -= 1


if __name__ == "__main__":
    random.seed(0)
    D = SkipList()

    print(len(D))
    D[20] = 2
    D[55] = 2
    D[12] = 20
    D[50] = 25
    D[44] = -2
    D[31] = 2
    D[17] = 4
    D[25] = 2
    D[39] = 2
    D[42] = 2
    D[38] = 2

    print(D[50])
    print(D[44])
    print(D.get(99, "Key doesn't exist"))
    del D[39]
    print(D.get(39, "key doesn't exist"))
    print(D.setdefault(57, 9))
    print(D.setdefault(55, 9))
    print(55 in D)

    for k, v in D.items():
        print(k, v)
