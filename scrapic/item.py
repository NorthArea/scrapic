import time


def get_time():
    return int(time.time())


class Item:
    def __init__(self, val, ttl=0):
        self._is_alive = True
        self._create_timestamp = get_time()
        self._val = val
        self._ttl = ttl

    def val(self):
        return self._val

    def is_alive(self) -> bool:
        if self._ttl == 0:
            return self._is_alive
        return self._ttl > get_time() - self._create_timestamp

    def destroy(self):
        self._is_alive = False
