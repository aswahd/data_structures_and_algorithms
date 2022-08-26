from general_tree import LinkedTree
from queue_linked_list import LinkedQueue
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

queue = LinkedQueue()
queue.enqueue(tree.root())


while not queue.is_empty():
    p = queue.dequeue()
    print(p.element())

    for child in tree.children(p):
        queue.enqueue(child)
