#!/usr/bin/env python3
"""
Defines the class Cache
"""
import redis
import uuid

class Cache:
    """Declares a Cache class"""
    def __init__(self) -> None:
        """Creates a connection to redis and flushes the db"""
        self.__redis: redis.Redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Adds a record in redis and returns the key"""
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key