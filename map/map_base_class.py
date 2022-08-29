from collections.abc import MutableMapping


class MapBase(MutableMapping):

    class _Item:

        __slots__ = "key", "value"

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, other):
            return self.key == other.key

        def __lt__(self, other):
            return self.key < other.key

    def __len__(self):
        pass

    def __getitem__(self, k):

        pass

    def __setitem__(self, key, value):

        pass

    def __delitem__(self, key):
        pass

    def __iter__(self):
        pass

