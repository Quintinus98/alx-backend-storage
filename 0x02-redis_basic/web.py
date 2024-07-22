#!/usr/bin/env python3
""" Redis Module """

from functools import wraps
import redis
import requests
from typing import Callable

redis_client = redis.Redis()


def cache_page(method: Callable) -> Callable:
    """Decortator for Caching"""

    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper for decorator"""
        redis_client.incr(f"count:{url}")
        cached_content = redis_client.get(f"cache:{url}")
        if cached_content:
            return cached_content.decode("utf-8")

        content = method(url)
        redis_client.setex(f"cache:{url}", 10, content)
        return content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Obtain the HTML content of a URL"""
    req = requests.get(url)
    return req.text
