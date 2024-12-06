import time


class ExpireCache:
    """
    A simple cache implementation that expires after a certain time.
    Each record in the cache has a key, data, and expire time.
    This class is not specific to the weather API and can be used in other projects.
    A most basic implementation.

    Attributes:
        expire_minutes (int): The number of minutes before the cache expires.
    """

    def __init__(self, expire_minutes: int = 5):
        self.cache = {}
        self.expire_minutes = expire_minutes

    def get_non_expired(self, key: str) -> dict | None:
        if key not in self.cache or self.__is_expired(key):
            return None
        return self.cache.get(key)["data"]

    def __is_expired(self, key: str) -> bool:
        return self.cache.get(key, {}).get("expire", 0) < time.time()

    def set(self, key: str, data: dict):
        self.cache[key] = {"data": data, "expire": time.time() + self.expire_minutes * 60}
