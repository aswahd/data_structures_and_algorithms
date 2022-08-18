class Empty(Exception):
  pass

class ArrayQueue:

  def __init__(self, cap=10):
    self._data = [None] * cap
    self._size = 0
    self.front = 0

  def __len__(self):
    return self._size

  def is_empty(self):
    return self._size == 0

  def enqueue(self, e):

    """Add e on the back"""

    if len(self._data) == self._size:
      # Resize
      self.resize(2 * len(self._data))

    back = (self.front + self._size) % len(self._data)
    self._data[back] = e
    self._size += 1

  def dequeue(self):
    """ Remove element from the front """
    if self.is_empty():
      raise Empty("Empty Queue!")

    elem = self._data[self.front]
    self._data[self.front] = None
    self.front = (self.front + 1) % len(self._data)
    self._size -= 1
    return elem

  def first(self):
    if self.is_empty():
      raise Empty('Empty Queuee!')

    return self._data[0]

  def resize(self, cap):
    old = self._data
    self._data = [None] * cap
    walk = self.front
    for i in range(self._size):
      self._data[i] = old[walk]
      walk = (walk + 1) % len(old)
    
    self.front = 0


