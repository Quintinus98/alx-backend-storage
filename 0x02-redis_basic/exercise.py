#!/usr/bin/env python3
"""REDIS Basics"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of the Cache class are called"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Calling decorated function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""
    input = f"{method.__qualname__}:inputs"
    output = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Call history"""
        self._redis.rpush(input, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output, str(result))
        return result

    return wrapper


def replay(method: Callable) -> None:
    """function to display the history of calls of a particular function"""
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for i, o in zip(inputs, outputs):
        print(f"{method_name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache:
    """Writing strings to Redis"""

    def __init__(self) -> None:
        """Initialize redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
