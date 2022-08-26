from tree_base_class import Tree


class BinaryTree(Tree):

    def left(self, p):
        """ Returns the position of the left child of the node at position p"""
        raise NotImplementedError()

    def right(self, p):
        """ Returns the position of the right child of the node at position p"""
        raise NotImplementedError()

    def sibling(self, p):
        """ Returns the position of the sibling of the node at position p"""
        parent = self.parent(p)
        if parent is None:
            # p is a root node
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """ Generates the position of the children of the node at position p """

        left = self.left(p)
        right = self.right(p)

        if left is not None:
            yield left

        if right is not None:
            yield right
