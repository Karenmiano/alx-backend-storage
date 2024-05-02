#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = 5.23
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": str,
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    print(cache.get_int(key))

print(cache.get(cache.store.__qualname__))
