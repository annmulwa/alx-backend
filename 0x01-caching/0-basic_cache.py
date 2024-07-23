#!/usr/bin/env python3
"""
Class BasicCache that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system.
    """
    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.
        """
        if key is None and item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
