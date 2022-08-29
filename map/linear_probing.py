from hash_map_base import HashMapBase


class LinearProbeHashMap(HashMapBase):

    """ Hash map implementation using linear probing collision handing method. """

    _AVAIL = object()   # to indicate locations of previous deletions

    def is_available(self, j):
        """
            Either empty or previously deleted location.
        """

        return self._table[j] is None or self._table[j] is LinearProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """ Find the next slot using linear probing
            Next slot is either
                None, or previously deleted location.
        """
        first_avail = None
        while True:

            if self.is_available(j):
                if first_avail is None:
                    first_avail = j   # this index will be used for __setitem__
                if self._table[j] is None:
                    return False, first_avail
            elif self._table[j].key == k:
                return True, j

            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        """ j: hash map """
        found, idx = self._find_slot(j, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))

        return self._table[j].value

    def _bucket_setitem(self, j, k, v):
        found, idx = self._find_slot(j, k)
        if not found:
            self._table[idx] = self._Item(k, v)
            self._n += 1
        else:
            self._table[idx].value = v

    def _bucket_delitem(self, j, k):
        found, idx = self._find_slot(j, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))

        self._table[idx] = LinearProbeHashMap._AVAIL   # deleted slot

    def __iter__(self):

        for j in range(len(self._table)):
            if not self.is_available(j):
                yield self._table[j].key


# Sanity check
if __name__ == "__main__":
    D = LinearProbeHashMap()

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
    print(D.popitem())
