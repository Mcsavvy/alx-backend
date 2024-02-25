#!/usr/bin/env python3
"""This implements LFU system,the least frequently used"""

from base_caching import BaseCaching


def pos(x, j, se=False):
    """Arranges the list in a LFU-LRU algorithm"""
    i = j
    x[i] += 1
    if se:
        while i + 1 < len(x) and x[i] > x[i + 1]:
            temp = x[i]
            x[i] = x[i + 1]
            x[i + 1] = temp
            i += 1
    if not se:
        while i - 1 >= 0 and x[i] < x[i - 1]:
            temp = x[i]
            x[i] = x[i - 1]
            x[i - 1] = temp
            i -= 1
    return i


class LFUCache(BaseCaching):
    """Uses LRU system to cache the data"""

    def __init__(self):
        """Initializes the cache
        """
        super().__init__()
        self.queue = []
        self.x = []

    def put(self, key, item):
        """Caches a new item and makes sure
        that it doesn't exceed the limit
        Args:
            key (str): the key of the item
            item (any): the item to be cached
        """
        if not (key and item):
            return
        if key in self.queue:
            i = self.queue.index(key)
            index = pos(self.x, i, True)
        else:
            self.queue.append(key)
            self.x.append(0)
            i = len(self.queue) - 1
            index = pos(self.x, i)
        if index != i:
            self.queue.remove(key)
            self.queue.insert(index, key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            x = self.queue.pop(0)
            self.x.pop(0)
            self.cache_data.pop(x, None)
            print(f"DISCARD: {x}")

    def get(self, key):
        """Retrieves a value

        Args:
            key (str): the key of the value

        Returns:
            _type_: _description_
        """
        if not (key and key in self.cache_data):
            return
        i = self.queue.index(key)
        pos(self.x, i)
        return self.cache_data[key]
