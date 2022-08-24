from doubly_linked_list_base import DoublyLinkedListBase


class PositionalList(DoublyLinkedListBase):
    class Position:

        def __init__(self, container, node):
            self._container = container  # the list
            self._node = node

        def element(self):
            return self._node._elem

        def __eq__(self, other):
            return self._node is other._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        # Invalid position
        # 1. If it is not a valid Position type
        # 2. If the node is not part of the list
        # 3. If the node is deprecated
        node = p._node
        # A different type
        if not isinstance(p, self.Position):
            raise TypeError("Incorrect position type!")
        # Not part of this list
        if p._container is not self:
            raise ValueError("p should belong to this list!")
        # Deprecated node
        if node._next is None:
            raise ValueError("Deprecated node!")
        return p._node

    def _make_position(self, node):

        if node is self._trailer or node is self._header:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        walk = self.first()
        while walk is not None:
            yield walk.element()
            walk = self.after(walk)

    def insert_between(self, e, predecessor, successor):
        # predecessor, and successor are both nodes
        node = super().insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self.insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self.insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, e, p):
        node = self._validate(p)
        return self.insert_between(e, node._prev, node)

    def add_after(self, e, p):
        node = self._validate(p)
        return self.insert_between(e, node, node._next)

    def replace(self, e, p):
        node = self._validate(p)
        old_value = node._elem
        node._elem = e
        return old_value

    def delete(self, p):
        node = self._validate(p)
        return self.delete_node(node)


if __name__ == "__main__":
    D = PositionalList()
    D.add_first(1)
    D.add_last(2)
    D.delete(D.after(D.first()))
    D.add_last(3)
    D.add_last(4)
    D.add_last(10)

    for el in D:
        print(el)

