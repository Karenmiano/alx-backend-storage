#!/usr/bin/env python3
"""
Defines the class Cache
"""
import redis
from typing import Union, Callable, Optional
import uuid


class Cache:
    """Declares a Cache class"""
    def __init__(self):
        """Creates a connection to redis and flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Adds a entry to redis and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, bytes, float]:
        """Retrieves an entry from redis and returns the value"""
        value = self._redis.get(key)
        if fn:
            try:
                value = fn(value)
            except Exception:
                pass
        return value

    def get_str(self, key: str):
        """Retrieves a string entry from redis and returns the value"""
        return self.get(key, str)

    def get_int(self, key: str):
        """Retrieves an integer entry from redis and returns the value"""
        return self.get(key, int)
