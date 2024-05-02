#!/usr/bin/env python3
"""
Defines the class Cache
"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(meth: Callable) -> Callable:
    """Decorator function that counts the number of times a
       methods of Cache class called"""
    @wraps(meth)
    def counter(self, *args, **kwargs):
        """Stores the counts in redis"""
        self._redis.incr(meth.__qualname__)
        return meth(self, *args, **kwargs)
    return counter


class Cache:
    """Declares a Cache class"""
    def __init__(self):
        """Creates a connection to redis and flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Adds a entry to redis and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Returns the value linked to the key"""
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """automatically parametrize Cache.get with the correct
        conversion function"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """automatically parametrize Cache.get with the correct
        conversion function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
