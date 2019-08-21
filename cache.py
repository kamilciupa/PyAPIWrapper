class Cache:

    cache_size = 5
    cache = dict()
    index = list()

    def is_cache_full(self):
        if len(self.index) >= self.cache_size:
            return True
        else:
            return False

    def drop_cache(self):
        self.cache.clear()

    def push_to_cache(self, key, value):
        self.cache[key] = value
        self.index.append(key)

    def delete_oldest(self):
        del self.cache[self.index[0]]
        self.index.pop(0)

    def add_entry(self, key, value):
        if self.is_cache_full():
            self.delete_oldest()
        self.push_to_cache(key, value)
