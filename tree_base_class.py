class Tree:

    class Position:

        def element(self):
            raise NotImplementedError()

        def __eq__(self, other):
            raise NotImplementedError()

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        """ Returns the position of the root node """
        raise NotImplementedError()

    def parent(self, p):
        """ Returns the position of the parent node of p """
        raise NotImplementedError()

    def num_children(self, p):
        """ Returns the number of children of node at p """
        return NotImplementedError()

    def children(self, p):
        """ Return the position of the children of node at p """
        raise NotImplementedError()

    def __len__(self):
        """ Returns the number of node of the tree """
        raise NotImplementedError()

    def is_empty(self):
        return len(self) == 0

    def is_root(self, p):
        """ Returns if the node at position p is a root node """
        return self.root() == p

    def is_leaf(self, p):
        """ Returns if the node at position p is a leaf node """

        return self.num_children(p) == 0

    def _depth(self, p):
        """ The number of parent nodes """
        if self.is_root(p):
            return 0
        else:
            return 1 + self._depth(self.parent(p))

    def depth(self, p=None):

        if p is None:
            p = self.root()
        return self._depth(p)

    def _height(self, p):
        """ The maximum number length of a path from node at p to a leaf node """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max([self._height(child) for child in self.children(p)])

    def height(self, p=None):
        """ The maximum number length of a path from node at p to a leaf node """
        if p is None:
            p = self.root()
        return self._height(p)
