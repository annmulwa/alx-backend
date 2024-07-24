#!/usr/bin/python3
"""
Class LRUCache that inherits from BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        Initializes Cache
        """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """
        Assign an item to the dictionary
        """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
        Return the value in self.cache_data linked to key
        """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
