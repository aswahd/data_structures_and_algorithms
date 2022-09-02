import random
from map_base_class import MapBase


class PositionalList:
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
        return self.Position(node, self)

    def __init__(self):
        self.start = self.header = None
        self.size = 0       # the size of the list

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # def first(self):
    #     """ Returns the position of the first element. """
    #     return self.make_position(self._header._next)
    #
    # def last(self):
    #     """ Returns the position of the last element. """
    #     return self.make_position(self._trailer._prev)

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

    # def insert_between(self, element, predecessor, successor):
    #     """ Insert element between predecessor, and successor, and return its position. """
    #     node = self.Node(predecessor, successor, None, None, element)
    #     predecessor._next = node
    #     successor._prev = node
    #     self.size += 1
    #
    #     return self.make_position(node)
    #
    # def add_first(self, element):
    #     """ Add first node. """
    #     return self.insert_between(element, self._header, self._header._next)
    #
    # def add_last(self, element):
    #     """ Add last node. """
    #
    #     return self.insert_between(element, self._trailer._prev, self._trailer)

    # def delete_node(self, node):
    #     node._prev._next = node._next
    #     node._next._prev = node._prev
    #     result = node._element
    #     node._prev = node._below = node._above = node._element = None
    #     self.size -= 1
    #     return result
    #
    # def delete(self, p):
    #     """ Delete the node at position p. """
    #     node = self._validate(p)
    #     return self.delete_node(node)

    # def add_after(self, element, p):
    #     """ Add element after position p. """
    #     node = self._validate(p)
    #     return self.insert_between(element, node, node._next)
    #
    # def add_before(self, element, p):
    #     """ Add element before position p. """
    #     node = self._validate(p)
    #
    #     return self.insert_between(element, node._prev, node)
    #
    # def replace(self, element, p):
    #     """ Replace the value at position p by element. """
    #     node = self._validate(p)
    #     result = node._element
    #     node._element = element
    #     return result

    def first(self):
        """ Returns the position of the first item in the first level of the list. """
        return self.make_position(self.header)

    def insert_after_above(self, p, q, e):
        """
            Insert (k, v) after position p, and above position q.
        """
        p_node = self._validate(p)
        q_node = self._validate(q)

        new = self.Node(p_node, p_node._next, q_node, q_node._above, e)
        p_node._next._prev = new
        q_node._above = new
        self.size += 1
        return self.make_position(new)

    def __iter__(self):
        walk = self.first()

        while self.next(walk) is not None:
            walk = self.next(walk)
            yield walk.element()


class SkipList(MapBase):

    class Item:
        __slots__ = "key", "value"

        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.list = PositionalList()
        self.height = 0  # the height of the skip list
        self.size = 0  # the size of the list

        # Add sentinel keys
        self.start = self.header = self.insert_after_above(None, None, self.Item(float('-inf'), None))
        self.insert_after_above(None, None, self.Item(float('inf'), None))

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

        walk = self.list.next(self.list.header)
        for i in range(len(self)):
            yield walk.element().key

    def __delitem__(self, key):
        self.delete(key)

    def insert_after_above(self, p, q, e):
        """
            Insert (k, v) after position p, and above position q.
        """
        return self.list.insert_after_above(p, q, e)

    def search(self, key):
        """ Return the position of the item with a key less than or equal to k or None if such a
        key doesn't exist. """

        p = self.start
        # down scanning
        while self.list.below(p) is not None:
            p = self.list.below(p)
            # forward scanning
            while key >= self.list.next(p).element().key:
                p = self.list.next(p)

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
                tail = self.list.next(self.start)
                self.start = self.list.insert_after_above(None, self.start, self.Item(-float('inf'), None))
                self.list.insert_after_above(self.start, tail, self.Item(float('inf'), None))

            q = self.list.insert_after_above(p, q, self.Item(key, value))
            while self.list.above(p) is None:
                p = self.list.prev(p)
            p = self.list.above(p)
            if not random.randrange(2):
                break

        self.size += 1

    def delete(self, key):
        """ Delete the item with key k. """
        p = self.search(key)
        if p.element().key != key:
            raise KeyError("Key Error: " + repr(key))

        while p is not None:
            above = self.list.above(p)
            self.list.delete(p)
            p = above
        self.size -= 1


if __name__ == "__main__":
    D = SkipList()

    print(len(D))
    D['K'] = 2
    D['B'] = 4
    D['U'] = 2
    D['V'] = 8
    D['K'] = 9
    print(D['B'])
    # print(D['X'])
    print(D.get('F', None))
    print(D.get('F', 5))
    print(D.get('K', 5))
    print(len(D))
    del D['V']
    print(D.pop('K'))
    print(D.keys())
    print(D.values())
    print(D.items())
    print(D.setdefault('B', 1))
    print(D.setdefault('A', 1))
    for k in D.keys():
        print(k, end=' ')
    print()
    print(D.popitem())
