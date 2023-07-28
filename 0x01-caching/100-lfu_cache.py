#!/usr/bin/python3
"""A caching system LFU implementation"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """implements put and get methods"""
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()
        self.item_frequency = {}
        self.frequency_lists = {}

    def update_frequency(self, key):
        """ Update the frequency of an item """
        if key in self.item_frequency:
            self.item_frequency[key] += 1
        else:
            self.item_frequency[key] = 1

    def update_frequency_list(self, key):
        """ Update the list of items based on their frequency """
        freq = self.item_frequency[key]
        if freq in self.frequency_lists:
            self.frequency_lists[freq].discard(key)
        else:
            self.frequency_lists[freq] = set()

        self.frequency_lists[freq + 1] = self.frequency_lists.get(
            freq + 1, set())
        self.frequency_lists[freq + 1].add(key)

    def get_least_frequent(self):
        """ Get the least frequent item from the cache """
        least_freq = min(self.frequency_lists)
        item_to_discard = self.frequency_lists[least_freq].pop()
        if not self.frequency_lists[least_freq]:
            del self.frequency_lists[least_freq]
        return item_to_discard

    def put(self, key, item):
        """puts a value"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if not self.item_frequency:
                return

            item_to_discard = self.get_least_frequent()
            del self.cache_data[item_to_discard]
            del self.item_frequency[item_to_discard]
            print("DISCARD:", item_to_discard)

        self.cache_data[key] = item
        self.update_frequency(key)
        self.update_frequency_list(key)

    def get(self, key):
        """gets a value"""
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        self.update_frequency_list(key)

        return self.cache_data[key]
