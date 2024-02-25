#!/usr/bin/env python3
"""This implements FIFO system, first in, first out
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Uses FIFO system to cache the data"""

    def __init__(self):
        """Initializes the cache
        """
        super().__init__()

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
        if len(self.cache_data) > self.MAX_ITEMS:
            dIter = iter(self.cache_data.items())
            first_key, first_value = next(dIter)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Retrieves a value

        Args:
            key (str): the key of the value

        Returns:
            _type_: _description_
        """
        if key:
            return self.cache_data.get(key, None)
