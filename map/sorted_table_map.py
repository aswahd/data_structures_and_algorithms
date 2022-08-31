from map_base_class import MapBase


class SortedTableMap(MapBase):

    def __init__(self):
        self._table = []

    def find_index(self, k, low, high):
        """ Return the index of the key that is greater than or equal to k. """
        if low > high:
            return high + 1
        else:
            mid = (low + high) // 2

            if k == self._table[mid].key:
                return mid
            else:
                if k < self._table[mid].key:
                    return self.find_index(k, low, mid - 1)
                else:
                    return self.find_index(k, mid + 1, high)

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        """ Return the value of associate with the key k. """
        j = self.find_index(k, 0, len(self._table) - 1)

        # if the key exists, it is at index j
        if j == len(self) or self._table[j].key != k:
            raise KeyError("Key Error: " + repr(k))

        return self._table[j].value

    def __setitem__(self, key, value):
        """
        If the key exists, replace its value with value.
        If the key doesn't exist, insert it at the right location.

        """

        j = self.find_index(key, 0, len(self) - 1)

        if j < len(self) and self._table[j].key == key:
            self._table[j].value = value
        else:
            self._table.insert(j, self._Item(key, value))

    def __delitem__(self, key):
        """
            Delete (key, value) if the exists, or raise an error.
        """

        j = self.find_index(key, 0, len(self) - 1)

        if j == len(self) or self._table[j].key != key:
            raise KeyError("Key Error: " + repr(key))

        self._table.pop(j)

    def __iter__(self):
        for item in self._table:
            yield item.key

    def __reversed__(self):
        """ Iterate across all keys in reverse order (non-increasing order). """

        for item in reversed(self._table):
            yield item.key

    def find_min(self):
        """ Return the minimum key from the search table, or None if it is empty. """
        try:
            return self._table[0].key, self._table[0].value
        except IndexError:
            return None

    def find_max(self):
        """ Return the maximum key from the search table, or None if it is empty. """
        try:
            return self._table[-1].key, self._table[-1].value
        except IndexError:
            return None

    def find_lt(self, k):
        """ Return (k, v) pairs of a key that is less than k, or None if it doesn't exist. """
        j = self.find_index(k, 0, len(self) - 1)
        if j > 0:
            return self._table[j - 1].key, self._table[j - 1].value
        return None

    def find_le(self, k):
        """ Return (k, v) pairs of a key that is less than or equal to k, or None if it doesn't exist. """
        j = self.find_index(k, 0, len(self) - 1)
        if j > 0:
            if self._table[j].key == k:
                j -= 1
            return self._table[j - 1].key, self._table[j - 1].value
        else:
            return None

    def find_gt(self, k):
        """ Return (k, v) pairs of a key that is greater than k, or None if it doesn't exist. """

        j = self.find_index(k, 0, len(self) - 1)

        if self._table[j].key == k:
            j += 1

        if j == len(self):
            return None
        else:
            return self._table[j].key, self._table[j].value

    def find_ge(self, k):
        """ Return (k, v) pairs of a key that is greater than k or equal, or None if it doesn't exist. """

        j = self.find_index(k, 0, len(self) - 1)

        if j == len(self):
            return None

        return self._table[j].key, self._table[j].value

    def find_range(self, start, stop):
        """ Iterate across all keys (non-decreasing order) """


# sanity check
if __name__ == "__main__":
    D = SortedTableMap()
    print(len(D))
    D['K'] = 2
    D['B'] = 4
    D['U'] = 2
    D['V'] = 8
    D['K'] = 9
    print(D['B'])
    # print(D['X'])
    print(D.get('F', None))
    print(D.get('F', 5))
    print(D.get('K', 5))
    print(len(D))
    del D['V']
    print(D.pop('K'))
    print(D.keys())
    print(D.values())
    print(D.items())
    print(D.setdefault('B', 1))
    print(D.setdefault('A', 1))
    for k in D.keys():
        print(k, end=' ')
    print()
    print(D.popitem())
