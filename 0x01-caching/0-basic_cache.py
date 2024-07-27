#!/usr/bin/env python3
"""Basic caching module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """represents object that allows storing, 
    retrieving items from a dictionary"""
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieves item by key"""
        return self.cache_data.get(key, None)
