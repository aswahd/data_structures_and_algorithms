from binary_tree_linked_list import LinkedBinaryTree
from map.map_base_class import MapBase


class BinarySearchTree(MapBase):
    class Item:
        __slot__ = "key", "value"

        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value

    def __init__(self) -> None:
        super().__init__()

        self.table = LinkedBinaryTree()

    def __len__(self):
        return len(self.table)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        p = self.search(self.table.root(), k)

        if k == p.element().key:
            return p.element().value

        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        if self.is_empty():
            self.table.add_root(self.Item(k, v))
            return

        self.insert(k, v)

    def __delitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))

        self.delete(k)

    def __iter__(self):
        walk = self.first()

        while walk is not None:
            yield walk.element().key
            walk = self.after(walk)

    def is_empty(self):

        return len(self) == 0

    def before(self, p):
        """ Return the position the node that comes before p in an
        inorder traversal.
        """

        if self.table.left(p) is not None:
            return self.last(self.table.left(p))
        else:
            # the first ancestor such that p is a right successor, comes before p.
            walk = p
            ancestor = self.table.parent(walk)

            while ancestor is not None and self.table.right(ancestor) != walk:
                walk = ancestor
                ancestor = self.table.parent(walk)

            return ancestor

    def after(self, p):
        """ Return the position of the node that comes after p
            in an inorder traversal.
        """

        if self.table.right(p) is not None:
            # the leftmost child of the right child comes next. 
            walk = self.table.right(p)

            while self.table.left(walk) is not None:
                walk = self.table.left(walk)

            return walk

        else:
            # the ancestor of p such that p is the left child comes next.
            walk = p
            ancestor = self.table.parent(walk)
            while ancestor is not None and walk != self.table.left(ancestor):
                walk = ancestor
                ancestor = self.table.parent(walk)

            return ancestor

    def search(self, p, key):
        """ search key starting from position p.
            If key doesn't exist, return the position before/after it.
         """

        node = self.table._validate(p)

        if key == node._elem.key:
            return p
        elif key < node._elem.key and self.table.left(p) is not None:
            return self.search(self.table.left(p), key)
        elif key > node._elem.key and self.table.right(p) is not None:
            return self.search(self.table.right(p), key)

        return p

    def insert(self, k, v):
        """ Insert (k, v) at appropriate place. """

        p = self.search(self.table.root(), k)

        if k == p.element().key:
            p.element().value = v
        else:
            if k < p.element().key:
                # insert on the left
                self.table.add_left(p, self.Item(k, v))
            else:
                self.table.add_right(p, self.Item(k, v))

    def delete(self, key):
        """ Delete key. """

        p = self.search(self.table.root(), key)

        if p.element().key != key:
            raise KeyError("Key Error: " + repr(key))

        if self.table.num_children(p) < 2:
            self.table.delete(p)
        else:
            # p has left and right children
            # replace its value with what before it (the right most position of the
            # left subtree. The rightmost position has at most one child[i.e., left child].)
            r = self.before(p)
            p.element().key = r.element().key
            p.element().value = r.element.value
            self.table.delete(r)

    def first(self):
        """  Return the position containing the least key. """
        if self.is_empty():
            return None

        walk = self.table.root()

        while self.table.left(walk) is not None:
            walk = self.table.left(walk)

        return walk

    def last(self, p=None):
        """ Return the position containing the greatest key. """
        if self.is_empty():
            return None
        if p is None:
            p = self.table.root()

        while self.table.right(p) is not None:
            p = self.table.right(p)
        return p

    def find_min(self):
        """ Return (k, v) with the minimum key. """

        try:
            first = self.first()
            return first.element().key, first.element().value
        except KeyError:
            return None

    def find_max(self):
        """ Return (k, v) with the maximum key. """
        try:
            last = self.last()
            return last.element().key, last.element().value
        except KeyError:
            return None

    def __reversed__(self):
        """ Return an iterator in decreasing order of keys. """
        walk = self.last()
        while walk is not None:
            yield walk.element().key
            walk = self.before(walk)

    # template functions for tree rebalancing
    def _rebalance_insert(self, p): pass
    def _rebalance_delete(self, p): pass
    def _rebalance_access(self, p): pass

    def _relink(self, parent, child, make_left_child):
        """ Link child-parent"""

        if make_left_child:
            parent._left = child
        else:
            parent._right = child

        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        """ Rotate position p with its parent. """
        x = p._node
        y = x._parent
        z = y._parent

        if z is None:
            self.table._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)

        if x == y._left:
            self._relink(y, x._right, True)   # make x._right the left child of y
            self._relink(x, y, False)         # make y the right child of x
        else:
            self._relink(y, x._left, False)   # make x._left the right child of y
            self._relink(x, y, True)

    def _restructure(self, x):
        """ Trinode balancing of a tree at position x. """
        y = self.table.parent(x)
        z = self.table.parent(y)

        if (x == self.table.right(y)) == (y == self.table.right(z)):
            # single rotation
            # / z
            # / y
            # / x

            # or
            # \ z
            # \ y
            # \ x
            self._rotate(y)
            return y
        else:
            # double rotation
            self._rotate(x)
            self._rotate(x)
            return x


if __name__ == "__main__":
    D = BinarySearchTree()

    D[50] = 25
    D[44] = -2
    D[31] = 2
    D[27] = 4
    D[17] = 4
    D[25] = 2
    D[-1] = 2
    D[-2] = 2
    D[39] = 2
    D[42] = 2
    D[12] = 2
    D[38] = 21
    D[-1] = 10

    print("------------ Sort Methods ------------")
    print("min key: ", D.find_min())
    print("max key: ", D.find_max())

    for k in D:
        print(k)
    print("------------ Reverse Order ------------")
    for k in reversed(D):
        print(k)
