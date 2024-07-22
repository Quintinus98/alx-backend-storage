#!/usr/bin/env python3
"""REDIS Basics"""
import redis
from uuid import uuid4


class Cache:
    """Writing strings to Redis"""

    def __init__(self) -> None:
        """Initialize redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | float) -> str:
        "Store data"
        key = str(uuid4())
        self._redis.append(key=key, value=data)
        return key
