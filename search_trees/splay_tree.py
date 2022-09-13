from search_trees.binary_search_tree import BinarySearchTree


class SplayTree(BinarySearchTree):

    def _splay(self, p):

        while p != self.root():
            parent = self.parent(p)
            g_parent = self.parent(parent)

            if g_parent is None:
                self._rotate(p)
            elif (parent == self.left(g_parent)) == (p == self.left(parent)):
                self._rotate(parent)
                self._rotate(p)
            else:
                self._rotate(p)
                self._rotate(p)

    def _rebalance_insert(self, p):
        self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)


D = SplayTree()

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
