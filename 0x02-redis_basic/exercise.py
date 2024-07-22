#!/usr/bin/env python3
"""REDIS Basics"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Writing strings to Redis"""

    def __init__(self) -> None:
        """Initialize redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float]) -> str:
        "Store data"
        key = str(uuid4())
        self._redis.set(name=key, value=data)
        return key
