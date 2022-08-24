import random
from doubly_linked_positional_list import PositionalList

values = [random.randint(-10, 10) for _ in range(6)]
print(values)

# Create a position list
pos_list = PositionalList()
for v in values:
    pos_list.add_last(v)

# Insertion sort
if len(pos_list) > 1:
    curr = pos_list.first()

    while curr != pos_list.last():
        pivot = pos_list.after(curr)
        value = pivot.element()
        if value > curr.element():
            # Already in increasing order
            curr = pivot
        else:
            walk = curr
            while walk != pos_list.first() and pos_list.before(walk).element() > value:
                walk = pos_list.before(walk)
            pos_list.delete(pivot)
            pos_list.add_before(walk, value)

for v in pos_list:
    print(v)

