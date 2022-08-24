from stack_singly_linked_list import LinkedStack
# Build a linked list
array = LinkedStack()
array.push(1)
array.push(10)
array.push(5)
array.push(2)
# Reverse the linked list


def reverse(l, tail=None):
    next = l._head._next
    l._head._next = tail  # the current head becomes next to the tail
    if next is None:
        return l
    else:
        new_tail = l._head
        l._head = next          # the next item becomes the new head
        return reverse(l, new_tail)


linked_list = reverse(array)
walk = array._head
while walk is not None:
    print(walk._elem)
    walk = walk._next