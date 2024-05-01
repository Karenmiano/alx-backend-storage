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
