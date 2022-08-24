class Empty(Exception):
    pass


class DequeArray:

    def __init__(self, cap=10):
        self._front = 0
        self._data = [None] * cap
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        self.assert_not_empty()
        return self._data[self._front]

    def add_first(self, e):
        if self._size == len(self._data):
            self.resize(len(self._data) * 2)

        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def assert_not_empty(self):
        if self.is_empty():
            raise Empty('Empty Queue!')

    def delete_first(self):
        self.assert_not_empty()
        if self._size < len(self._data) // 4:
            self.resize(len(self._data) // 2)
        result = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)
        self._data[self._front] = None
        self._size -= 1
        return result

    def add_last(self, e):
        if self._size == len(self._data):
            self.resize(len(self._data) * 2)
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def delete_last(self):
        self.assert_not_empty()
        back = (self._front + self._size - 1) % len(self._data)
        result = self._data[back]
        self._data[back] = None
        self._size -= 1
        return result

    def last(self):
        self.assert_not_empty()
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap

        for i in range(self._size):
            self._data[i] = old[(self._front + i) % len(old)]
        self._front = 0


if __name__ == "__main__":
    ds = DequeArray(cap=5)
    ds.add_last(5)
    ds.add_first(3)
    ds.add_first(7)
    print(ds.first())
    print(ds.delete_last())
    print(len(ds))
    print(ds.delete_last())
    print(ds.delete_last())
    ds.add_first(6)
    print(ds.last())
    ds.add_first(8)
    print(ds.is_empty())
    print(ds.last())
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(5)
    ds.add_first(10)
    print(len(ds))
    print(ds.first())

