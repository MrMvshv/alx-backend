#!/usr/bin/python3
"""A caching system that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """implements put and get methods"""
    def put(self, key, item):
        """puts a value"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """gets a value"""
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]