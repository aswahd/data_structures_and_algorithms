from hash_map_base import HashMapBase
from unsorted_map import UnsortedMap


class ChainHashMap(HashMapBase):
    """ Separate chaining implementation of a hash table. """

    def _bucket_getitem(self, j, k):
        """
            j: index in the hash table
            k: key in the hash bucket
        """
        bucket = self._table[j]

        if bucket is None:
            # Key doesn't exist
            raise KeyError("Key Error: " + repr(k))

        return bucket[k]    # Possibly non-existent key

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedMap()
        old_size = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]

        if bucket is None:
            raise KeyError("Key Error: " + repr(k))

        del bucket[k]

    def __iter__(self):

        for bucket in self._table:
            if bucket is not None:
                for k in bucket:
                    yield k


# Sanity check
if __name__ == "__main__":
    D = ChainHashMap()

    print(len(D))
    D['K'] = 2
    D['B'] = 4
    D['U'] = 2
    D['V'] = 8
    D['K'] = 9
    print(D['B'])
    # print(D['X'])
    print(D.get('F'))
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
