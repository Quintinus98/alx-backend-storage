#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__("exercise").Cache
replay = __import__("exercise").replay

# cache = Cache()

# data = b"hello"
# key = cache.store(data)
# print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))

cache = Cache()

# TEST_CASES = {b"foo": None, 123: int, "bar": lambda d: d.decode("utf-8")}

# for value, fn in TEST_CASES.items():
#     key = cache.store(value)
#     print(value, sep="\t")
#     print(cache.get(key, fn=fn))
#     # assert cache.get(key, fn=fn) == value

cache.store("foo")
cache.store("bar")
cache.store("42")

replay(cache.store)
