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
    def wrapper(url: str) -> str:  # sourcery skip: use-named-expression
        """Wrapper for decorator"""
        redis_client.incr(f"count:{url}")
        cached_html = redis_client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode("utf-8")
        html = method(url)
        redis_client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Obtain the HTML content of a URL"""
    req = requests.get(url)
    return req.text
