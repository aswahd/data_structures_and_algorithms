from map_base_class import MapBase


class UnsortedMap(MapBase):

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):

        for item in self._table:

            if item.key == k:
                return item.value

        raise KeyError(f"Key error: " + repr(k))

    def __setitem__(self, key, value):

        for item in self._table:
            if item.key == key:
                item.value = value
                return
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        for i in range(len(self._table)):
            if self._table[i].key == key:
                self._table.pop(i)
                return

        raise KeyError("Key error: ", repr(key))

    def __iter__(self):
        for item in self._table:
            yield item.key


if __name__ == "__main__":
    d = UnsortedMap()

    for i in range(5):
        d[str(i)] = i

    print(d['3'])
    print(d.get('10', "Key doesn't exists!"))
    print(2 in d)
    print(6 in d)

    for k, v in d.items():
        print(k, v)

    print(d.setdefault('5', 5))


