from binary_tree_linked_list import LinkedBinaryTree

tree = LinkedBinaryTree()
tree.add_root('-')
left_1 = tree.add_left(tree.root(), '/')
left_2 = tree.add_left(left_1, 'x')
left_3 = tree.add_left(left_2, '+')
tree.add_left(left_3, 3)

tree.add_right(left_3, 1)
tree.add_right(left_2, 3)
left_2 = tree.add_right(left_1, '+')
left_3 = tree.add_left(left_2, '-')
tree.add_left(left_3, 9)
tree.add_right(left_3, 5)
tree.add_right(left_2, 2)

right_1 = tree.add_right(tree.root(), '+')
left_2 = tree.add_left(right_1, 'x')
tree.add_left(left_2, 3)

right_2 = tree.add_right(left_2, '-')
tree.add_left(right_2, 7)
tree.add_right(right_2, 4)
tree.add_right(right_1, 6)


def inorder(T, p=None):

    """ Inorder traversal of a binary tree """
    # visit the left subtree
    # visit p
    # visit the right subtree

    if p is None:
        p = T.root()

    def _inorder(T, p):

        left = T.left(p)
        if left is not None:
            _inorder(T, left)

        print(p.element())

        right = T.right(p)
        if right is not None:
            _inorder(T, right)

    return _inorder(T, p)


inorder(tree)
