class Empty(Exception):
    pass


class ArrayStack:

    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Empty stack!")

        return self._data[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):

        return len(self._data)
