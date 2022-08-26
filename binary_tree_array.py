from binary_tree_base_class import BinaryTree


class ArrayBinaryTree(BinaryTree):

    def __init__(self):
        self._root = 0
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def num_children(self, p):
        """ Returns the number of children at position p """
        left = 2 * p + 1
        right = 2 * p + 1
        count = 0
        if not (left > len(self._data) - 1) and self._data[left] is not None:
            count += 1

        if not (right > len(self._data) - 1) and self._data[right] is not None:
            count += 1

        return count

    def is_leaf(self, p):
        """ Returns if p is a leaf node. """
        return self.num_children(p) == 0

    def left(self, p):
        """ Returns the position of the left child """
        idx = 2 * p + 1
        if idx > (len(self._data) - 1) or self._data[idx] is None:
            return None
        return idx

    def right(self, p):
        """ Returns the position of the right child """
        idx = 2 * p + 2
        if idx > (len(self._data) - 1) or self._data[idx] is None:
            return None

        return idx

    def parent(self, p):
        """ Returns the position of the parent node """
        idx = (p - 1) // 2
        if idx < 0:
            return None

        return idx

    def add_root(self, e):
        """ Returns the position of the root node """
        if len(self._data) != 0:
            raise ValueError("root exists!")

        self._size += 1
        self._data.append(e)
        return 0

    def add_left(self, p, e):
        """ add e as the left child of position p """
        # Validate position p
        idx = 2 * p + 1
        if p > (len(self._data) - 1) or self._data[p] is None:
            raise ValueError("Invalid position")

        n = len(self._data)
        for _ in range(n, idx+1):
            self._data.append(None)
        self._data[idx] = e
        self._size += 1
        return idx

    def add_right(self, p, e):
        """ add e as the right child of position p """

        # Validate position p
        idx = 2 * p + 2
        if p > (len(self._data) - 1) or self._data[p] is None:
            raise ValueError("Invalid position")

        n = len(self._data)
        for _ in range(n, idx+1):
            self._data.append(None)
        self._data[idx] = e
        self._size += 1
        return idx

    def root(self):
        """ Returns the position of the root node """

        if len(self._data) == 0:
            return None

        return 0

    def replace(self, p, e):
        """ Replace the element at position p """
        if p > (len(self._data) - 1) or self._data[p] is None:
            raise ValueError("Invalid Position!")

        old_value = self._data[p]
        self._data[p] = e

        return old_value


# sanity check
if __name__ == "__main__":
    tree = ArrayBinaryTree()
    # [/, x, +, +, 4, -, 2, 3, 1, None, None, 9, 5]
    tree.add_root('/')
    tree.add_left(0, 'x')
    tree.add_right(0, '+')
    tree.add_left(1, '+')
    tree.add_right(1, 4)
    tree.add_left(3, 3)
    tree.add_right(3, 1)
    tree.add_left(2, '-')
    tree.add_right(2, 2)
    tree.add_left(5, 9)
    tree.add_right(5, 5)
    print(tree._data)
    print(len(tree))
    print(tree.depth(5))
    print(tree.height())



