from queue_linked_list import LinkedQueue
# Build a linked list
array = LinkedQueue()
array.enqueue(1)
array.enqueue(10)
array.enqueue(5)
array.enqueue(2)
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