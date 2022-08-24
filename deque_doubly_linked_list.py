from doubly_linked_list_base import DoublyLinkedListBase


class Deque(DoublyLinkedListBase):

    def first(self):
        self.assert_not_empty()
        return self._header._next._elem

    def last(self):
        self.assert_not_empty()
        return self._trailer._prev._elem

    def add_first(self, e):
        predecessor = self._header
        successor = self._header._next
        node = self.insert_between(e, predecessor, successor)
        return node

    def delete_first(self):
        self.assert_not_empty()
        return self.delete_node(self._header._next)

    def add_last(self, e):
        predecessor = self._trailer._prev
        successor = self._trailer
        self.insert_between(e, predecessor, successor)

    def delete_last(self):
        self.assert_not_empty()
        node = self._trailer._prev
        result = self.delete_node(node)
        return result


if __name__ == "__main__":
    D = Deque()
    D.add_first(1)
    D.add_last(3)
    D.add_last(5)
    D.add_last(4)
    D.add_last(2)
    # {1, 3, 5, 4, 2}
    D.delete_last()
    D.delete_last()
    D.delete_first()
    D.delete_first()

    print(D.first(), D.last())

