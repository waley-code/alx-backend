#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds a key value pair"""
        if ((key is not None) and (item is not None)):
            self.cache_data.update({key: item})

    def get(self, key):
        """returns a value for a key"""
        if key is None:
            return None
        returnKey = self.cache_data.get(key, None)
        if returnKey is None:
            return None
        return returnKey
