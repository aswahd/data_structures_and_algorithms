from binary_tree_linked_list import LinkedBinaryTree
from map.map_base_class import MapBase


class BinarySearchTree(LinkedBinaryTree, MapBase):

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element().key

        def value(self):
            return self.element().value
        
    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        p = self.search(self.root(), k)
        self._rebalance_access(p)
        if k != p.element().key:
            raise KeyError("Key Error: " + repr(k))
        return p.element().value

    def __setitem__(self, k, v):
        if self.is_empty():
            self.add_root(self._Item(k, v))
            return

        self.insert(k, v)

    def __delitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))

        self._delete(k)

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

        if self.left(p) is not None:
            return self.last(self.left(p))
        else:
            # the first ancestor such that p is a right successor, comes before p.
            walk = p
            ancestor = self.parent(walk)

            while ancestor is not None and self.right(ancestor) != walk:
                walk = ancestor
                ancestor = self.parent(walk)

            return ancestor

    def after(self, p):
        """ Return the position of the node that comes after p
            in an inorder traversal.
        """

        if self.right(p) is not None:
            # the leftmost child of the right child comes next. 
            walk = self.right(p)

            while self.left(walk) is not None:
                walk = self.left(walk)

            return walk

        else:
            # the ancestor of p such that p is the left child comes next.
            walk = p
            ancestor = self.parent(walk)
            while ancestor is not None and walk != self.left(ancestor):
                walk = ancestor
                ancestor = self.parent(walk)

            return ancestor

    def search(self, p, key):
        """ search key starting from position p.
            If key doesn't exist, return the position before/after it.
         """

        if key == p.key():
            return p
        elif key < p.key() and self.left(p) is not None:
            return self.search(self.left(p), key)
        elif key > p.key() and self.right(p) is not None:
            return self.search(self.right(p), key)

        return p

    def insert(self, k, v):
        """ Insert (k, v) at appropriate place. """

        p = self.search(self.root(), k)

        if k == p.key():
            p.element().value = v
            self._rebalance_access(p)
        else:
            if k < p.key():
                # insert on the left
                leaf = self.add_left(p, self._Item(k, v))
            else:
                leaf = self.add_right(p, self._Item(k, v))
            self._rebalance_insert(leaf)

    def _delete(self, key):
        """ Delete key. """

        p = self.search(self.root(), key)

        if p.key() != key:
            raise KeyError("Key Error: " + repr(key))

        if self.num_children(p) == 2:
            # p has left and right children
            # replace its value with what before it (the right most position of the
            # left subtree. The rightmost position has at most one child[i.e., left child].)
            r = self.before(p)
            self.replace(p, r.element())
            p = r
        parent = self.parent(p)
        self.delete(p)
        self._rebalance_delete(parent)

    def first(self):
        """  Return the position containing the least key. """
        if self.is_empty():
            return None

        walk = self.root()

        while self.left(walk) is not None:
            walk = self.left(walk)

        return walk

    def last(self, p=None):
        """ Return the position containing the greatest key. """
        if self.is_empty():
            return None
        if p is None:
            p = self.root()

        while self.right(p) is not None:
            p = self.right(p)
        return p

    def find_min(self):
        """ Return (k, v) with the minimum key. """

        try:
            first = self.first()
            return first.element().key, first.element().value
        except AttributeError:
            return None

    def find_max(self):
        """ Return (k, v) with the maximum key. """
        try:
            last = self.last()
            return last.element().key, last.element().value
        except AttributeError:
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
        x = p.node
        y = x._parent
        z = y._parent

        if z is None:
            self._root = x
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
        y = self.parent(x)
        z = self.parent(y)

        if (x == self.right(y)) == (y == self.right(z)):
            # single rotation
            # / z
            # / y
            # / x

            # or
            # \ z
            # \ y
            # \ x
            self._rotate(y)
            return y     # new root of the subtree
        else:
            # double rotation
            self._rotate(x)
            self._rotate(x)
            return x     # new root of the subtree


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
    print("------------ Deletion ------------")
    print("len before deletion: ", len(D))
    del D[50]
    del D[31]
    del D[-2]
    del D[42]
    del D[12]
    del D[-1]
    print("D[25] =", D[25])
    print("len after deletion: ", len(D))
    print("------------ Sort Methods ------------")
    print("min key: ", D.find_min())
    print("max key: ", D.find_max())

    for k in D:
        print(k)
    print("------------ Reverse Order ------------")
    for k in reversed(D):
        print(k)
