from binary_tree_base_class import BinaryTree


class LinkedBinaryTree(BinaryTree):

    class _Node:

        __slots__ = "_elem", "_left", "_right", "_parent"

        def __init__(self, element, left=None, right=None, parent=None):
            self._elem = element
            self._left = left
            self._right = right
            self._parent = parent

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node._elem

        def __eq__(self, other):
            """ """

            return type(self) is type(other) and self.node is other.node

    def _validate(self, p):
        """ """

        # invalid position
        # 1. if it is not a Position type
        # 2. if it is not part of this tree
        # 3. if it is a deprecated node

        if not isinstance(p, self.Position):
            raise TypeError("p is not a valid Position type!")

        if p.container is not self:
            raise ValueError("p is not part of this tree!")

        if p.node._parent is p.node: # convention for a deprecated node
            raise ValueError("p is deprecated!")

        return p.node

    def make_position(self, node):
        """ """

        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        """ Returns the position of the root node """
        return self.make_position(self._root)

    def parent(self, p):
        """ Returns the position of the parent node p """
        node = self._validate(p)
        return self.make_position(node._parent)

    def left(self, p):
        """ Returns the position of the left child of the node at position p"""
        node = self._validate(p)
        return self.make_position(node._left)

    def right(self, p):
        """ Returns the position of the right child of the node at position p"""
        node = self._validate(p)
        return self.make_position(node._right)

    def num_children(self, p):
        """ """
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1

        return count

    def add_root(self, e):
        """ """
        if self._root is not None:
            raise ValueError("root node exists!")
        self._root = self._Node(e, None, None, None)
        self._size = 1
        return self.make_position(self._root)

    def add_left(self, p, e):
        """ """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("left node exists!")
        left = self._Node(e, parent=node)
        node._left = left
        self._size += 1
        return self.make_position(left)

    def add_right(self, p, e):
        """ """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("right node exits!")
        right = self._Node(e, parent=node)
        node._right = right
        self._size += 1
        return self.make_position(right)

    def replace(self, p, e):
        """ Replace the element at position p by e, and return the old element """
        node = self._validate(p)
        old = node._elem
        node._elem = e
        return old

    def delete(self, p):
        """ """
        node = self._validate(p)
        if self.num_children(p) > 1:
            raise ValueError("node has two children!")

        child = node._left if node._left else node._right
        parent = node._parent
        if child is not None:
            child._parent = parent
        old_value = node._elem
        if parent is None:
            # p is a root node
            # then child becomes the root node
            self._root = child
        else:
            if parent._left == node:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        return old_value

    def attach(self, p, t1, t2):
        """ Attach tree t1 and t2, and make p their parent """

        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("p must be a leaf node!")

        self._size = len(t1) + len(t2)
        if not t1.is_empty():
            # make t1 the left child
            node._left = t1._root
            t1._root._parent = node
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            # make t2 the right child
            node._right = t2._root
            t2._root._parent = node
            t2._root = None
            t2._size = 0


# Sanity check
if __name__ == "__main__":
    binary_tree = LinkedBinaryTree()
    root = binary_tree.add_root(3)
    p = binary_tree.add_left(root, 4)
    binary_tree.add_right(root, 5)
    binary_tree.add_left(p, 6)
    print(len(binary_tree))
    print(binary_tree.depth())
    print(binary_tree.height(p))

