from scrapic.item import Item


class Scrapic:
    def __init__(self):
        self._storage = {}
        self._closure_storage = {}

    def get(self, key: str, default=None):
        if key in self._storage.keys() and self._storage[key].is_alive():
            return self._storage[key].val()
        return default

    def set(self, key: str, value, ttl=0):
        self._storage[key] = Item(value, ttl)

    def closure(self, key: str, func, ttl=0):
        if callable(func) is not True:
            raise ValueError('The func must be callable')
        if key in self._closure_storage.keys() and self._closure_storage[key].is_alive():
            return self._closure_storage[key].val()
        self._closure_storage[key] = Item(func(), ttl)
        return self._closure_storage[key].val()
