#!/usr/bin/env python3
"""This implements the LRU Caching sstem ie
it removes the least recently used"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Uses LRU system to cache the data"""

    def __init__(self):
        """Initializes the cache
        """
        super().__init__()
        self.queue = []

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
            self.queue.remove(key)
        self.queue.append(key)
        if len(self.cache_data) >= self.MAX_ITEMS:
            curr = self.queue.pop(0)
            del self.cache_data[curr]
            print(f"DISCARD: {curr}")
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
