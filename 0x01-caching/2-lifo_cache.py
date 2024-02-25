#!/usr/bin/env python3
"""This implements LIFO system, last in, first out
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Uses LIFO system to cache the data"""

    def __init__(self):
        """Initializes the cache
        """
        super().__init__()
        self.last = None

    def put(self, key, item):
        """Caches a new item and makes sure
        that it doesn't exceed the limit
        Args:
            key (str): the key of the item
            item (any): the item to be cached
        """
        if not (key and item):
            return
        self.cache_data[key] = item
        if (len(self.cache_data)) > self.MAX_ITEMS:
            del self.cache_data[self.last]
            print(f"DISCARD: {self.last}")
        self.last = key

    def get(self, key):
        """Retrieves a value

        Args:
            key (str): the key of the value

        Returns:
            _type_: _description_
        """
        if key:
            return self.cache_data.get(key, None)
