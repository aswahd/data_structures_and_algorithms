from tree_base_class import Tree
from doubly_linked_positional_list import PositionalList


class LinkedTree(Tree):

    class _Node:
        __slots__ = "_element", "_parent", "_children"

        def __init__(self, element, parent, children):
            self._element = element
            self._parent = parent
            self._children = children  # Doubly Linked List

    class Position(Tree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            # Two positions are equal if they refer to the same node
            return self._node is other._node

    def _validate(self, p):
        # invalid position
        # 1. wrong type
        # 2. not part of this tree
        # 3. deprecated position
        if not isinstance(p, self.Position):
            raise ValueError("p should be a valid Position type!")

        if p._container is not self:
            raise ValueError("P is not part of this list!")

        if p._node._parent is p._node:
            raise ValueError("Deprecated Node!")

        return p._node

    def make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        """ Returns the position of the root node """
        return self.make_position(self._root)

    def add_root(self, e):
        if self.root() is not None:
            raise ValueError("Root exists!")

        self._root = self._Node(e, None, PositionalList())
        self._size += 1
        return self.make_position(self._root)

    def parent(self, p):
        """ Returns the position of the parent of p """
        node = self._validate(p)
        return self.make_position(node._parent)

    def num_children(self, p):
        """ Returns the number of children of the node at position p """
        node = self._validate(p)
        return 0 if node is None else len(node._children)

    def children(self, p):
        """ Generate an iteration of the children at p """
        node = self._validate(p)
        for child in node._children:
            yield self.make_position(child)

    def first(self, p):
        """ Returns the position of the first children at position p """
        node = self._validate(p)
        children = node._children   # positional list
        return self.make_position(children.first()._node)

    def last(self, p):
        """ Returns the position of the last children at position p """
        node = self._validate(p)
        children = node._children
        return self.make_position(children.last()._node)

    def add_first(self, p, e):
        """ Add e as the first child of p """
        node = self._validate(p)
        children = node._children
        self._size += 1
        new_node = self._Node(e, node, PositionalList())
        return self.make_position(children.add_first(new_node)._node)

    def add_last(self, p, e):
        """ Add e as the last child of p """
        node = self._validate(p)
        children = node._children
        self._size += 1
        new_node = self._Node(e, node, PositionalList())
        return self.make_position(children.add_last(new_node).element())

    def add_before(self, p, e):
        """ Add a node with element e before node at position p """
        if self.is_root(p):
            raise ValueError("You cannot add a sibling to a root node!")
        node = self._validate(p)
        # find siblings of `node`
        parent = node._parent
        children = parent._children  # positional list
        self._size += 1
        new_node = self._Node(e, node, PositionalList())
        return self.make_position(children.add_before(p, new_node).element())

    def add_after(self, p, e):
        """ Add a node with element e after node at position p """
        if self.is_root(p):
            raise ValueError("You cannot add a sibling to a root node!")
        node = self._validate(p)
        # find siblings of `node`
        parent = node._parent
        children = parent._children  # positional list
        self._size += 1
        new_node = self._Node(e, node, PositionalList())
        return self.make_position(children.add_after(p, new_node).element())

    def delete(self, p):
        """ Delete the node at position p """
        if self.is_root(p) and not self.is_leaf(p):
            raise ValueError("You cannot delete a root node with children!")
        node = self._validate(p)
        parent = node._parent
        children = node._children
        for child in children:
            child._parent = parent
        value = node._element
        # deprecate the deleted node
        node._parent = node
        node._children = None  # empty list
        self._size -= 1
        return value


# Sanity check
if __name__ == "__main__":

    tree = LinkedTree()
    root = tree.add_root("Electronics R'Us")
    tree.add_last(root, "R&D")
    sales = tree.add_last(root, "Sales")
    tree.add_last(root, "Purchasing")
    manufacturing = tree.add_last(root, "Manufacturing")
    tree.add_last(sales, 'Domestic')
    international = tree.add_last(sales, 'International')
    tree.add_last(manufacturing, "TV")
    tree.add_last(manufacturing, "CD")
    tree.add_last(manufacturing, "Tuner")
    tree.add_last(international, "Canada")
    tree.add_last(international, "S. America")
    overseas = tree.add_last(international, "Overseas")
    tree.add_last(overseas, "Africa")
    tree.add_last(overseas, "Europe")
    tree.add_last(overseas, "Asia")
    tree.add_last(overseas, "Australia")
    node = manufacturing._node._children
    for child in node:
        print(child._element)
