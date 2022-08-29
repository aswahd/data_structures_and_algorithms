import random
from map_base_class import MapBase


class HashMapBase(MapBase):

    def __init__(self, cap=11, p=109345121):
        self._table = [None] * cap
        self._n = 0         # the size of the table
        # MAD compression
        # ((scale * i + offset) % prime) % len(table)
        self._prime = p
        self._scale = 1 + random.randrange(p - 1)
        self._offset = random.randrange(p)

    def _hash_function(self, k):
        """ Use integer representation of k as the hash value"""

        return ((hash(k) * self._scale + self._offset) % self._prime) % len(self._table)

    def __len__(self):
        return self._n

    def _bucket_getitem(self, j, k):
        """ Returns the value associated with key k that is stored
         at the bucket indexed by j.
        """
        raise NotImplementedError("Not implemented.")

    def _bucket_setitem(self, j, k, v):
        """ Set (k, v) at bucket j. """
        raise NotImplementedError("Not implemented.")

    def _bucket_delitem(self, j, k):
        """ delete item identified by key k, located at bucket j."""
        raise NotImplementedError("Not implemented.")

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)

        if len(self) > len(self._table) // 2:       # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)   # usually a prime number

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, cap):
        """ Resize the size of the hash table """
        old_map = self.items()

        self._table = [None] * cap
        self._n = 0
        for k, v in old_map:
            self[k] = v   # hash value is recalculated

    def __iter__(self):
        """ Return an iterator of the items of the hash table. """
        raise NotImplementedError("Not implemented.")

