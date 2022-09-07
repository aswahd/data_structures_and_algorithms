from search_trees.binary_search_tree import BinarySearchTree
from binary_tree_linked_list import LinkedBinaryTree
from queue_linked_list import LinkedQueue


class AVLTree(BinarySearchTree, LinkedBinaryTree):

    class _Node(LinkedBinaryTree._Node):
        __slots__ = "_height"

        def __init__(self, element, left=None, right=None, parent=None, height=None):
            super().__init__(element, left, right, parent)
            self._height = height

    def _rebalance_delete(self, p):
        self._rebalance(p)

    def _rebalance_insert(self, p):
        self._rebalance(p)

    def left_height(self, p):
        return p.node._left._height if p.node._left is not None else 0

    def right_height(self, p):
        return p.node._right._height if p.node._right is not None else 0

    def _recompute_height(self, p):
        """ Returns the height of the subtree rooted at p. """
        h = 1 + max(self.left_height(p), self.right_height(p))
        p.node._height = h

    def is_balanced(self, p):
        return abs(self.left_height(p) - self.right_height(p)) <= 1

    def taller_child(self, p, choose_left=False):
        """ Returns p's child with higher height """
        if self.left_height(p) + choose_left > self.right_height(p):
            return self.left(p)
        else:
            return self.right(p)

    def tall_grand_child(self, p):
        """ Returns p's grand child with the highest height. """
        child = self.taller_child(p)
        return self.taller_child(child, choose_left=self.left(p) == p)

    def _rebalance(self, p):
        while p is not None:
            """ Balance tree after insertion or deletion. """
            old_height = p.node._height  # if height doesn't change, the balance requirement is satisfied
            if not self.is_balanced(p):
                p = self._restructure(self.tall_grand_child(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)  # height can change because of insertion or deletion

            if p.node._height == old_height:
                p = None
            else:
                p = self.parent(p)


if __name__ == "__main__":
    D = AVLTree()
    for i in range(10):
        D[i] = i

    print("height: ", D.height())
    print('------ Breadth First Traversal ------')
    queue = LinkedQueue()
    queue.enqueue(D.root())
    while not queue.is_empty():
        p = queue.dequeue()
        print(p.key())

        for child in D.children(p):
            queue.enqueue(child)

    print('------ Non-decreasing Order ------')

    for k in D:
        print(k)

