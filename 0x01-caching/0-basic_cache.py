#!/usr/bin/env python3
"""This is a simple caching system called BasicCache
that inherits from BaseCaching.
It does not have a limit on the number of items in the cache."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system
    """

    def __init__(self):
        """Initializes the cache
        """
        super().__init__()

    def put(self, key, item):
        """Caches a new item

        Args:
            key (str): the key of the item
            item (any): the item to be cached
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a value

        Args:
            key (str): the key of the value

        Returns:
            _type_: _description_
        """
        if key:
            return self.cache_data.get(key, None)
