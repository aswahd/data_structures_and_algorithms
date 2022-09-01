from platform import node
from xml.dom.minidom import Element


class SkipList:

    class _Node:

        __slots__ = ""

        def __init__(self, prev=None, next=None, below=None, above=None, element=None):
            self._element = element
            self._prev = prev
            self._next = next
            self._below = below
            self._above = above

    class Position:

        def __init__(self, node, container):
            self._node = node
            self._container = container

            
        def element(self):
            return self._node._element

        def __eq__(self, other):
            pass

        def __ne__(self, other):
            return not (self == other)

        
    def __init__(self):
        pass


