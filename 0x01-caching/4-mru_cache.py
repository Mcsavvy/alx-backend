#!/usr/bin/env python3
"""This implements LFU system, last in, first out
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Uses MRU system to cache the data"""

    def __init__(self):
        """Initializes the cache
        """
        super().__init__()
        self.last = None
        self.queue = []

    def put(self, key, item):
        """Caches a new item and makes sure
        that it doesn't exceed the limit
        Args:
            key (str): the key of the item
            item (any): the item to be cached
        """
        mark = False
        if not (key and item):
            return
        if key in self.queue:
            self.queue.remove(key)
        if len(self.queue) >= self.MAX_ITEMS:
            if mark:
                curr = self.queue[-1]
                self.queue.remove(curr)
            else:
                curr = self.queue.pop()
            del self.cache_data[curr]
            print(f"DISCARD: {curr}")

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves a value

        Args:
            key (str): the key of the value

        Returns:
            _type_: _description_
        """
        if not (key and key in self.cache_data):
            return
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
