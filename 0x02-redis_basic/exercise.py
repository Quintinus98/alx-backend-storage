#!/usr/bin/env python3
"""REDIS Basics"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """Writing strings to Redis"""

    def __init__(self) -> None:
        """Initialize redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data"""
        key = str(uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Convert data to fn format or None if not provided"""
        bValue = self._redis.get(name=key)
        if bValue is None:
            return None
        if fn is None:
            return bValue
        return fn(bValue)

    def get_str(self, key: str) -> str:
        """Convert data to str"""
        return self.get(key, lambda data: data.decode("utf-8"))

    def get_int(self, key: str, fn: Callable) -> int:
        """Convert data to int"""
        return self.get(key, lambda data: int(data))
