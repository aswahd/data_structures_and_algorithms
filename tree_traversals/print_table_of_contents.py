from general_tree import LinkedTree

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

# The table of content can be printed using the preorder traversal


def print_content(T):

    def _preorder(T, p, path, d):
        label = '.'.join(str(n + 1) for n in path)
        print(label + 2 * d * " ", p.element())
        path.append(0)
        for child in T.children(p):
            _preorder(T, child, path, d+1)
            path[-1] += 1
        path.pop()
    p = T.root()

    _preorder(T, p, [], 0)


print_content(tree)
