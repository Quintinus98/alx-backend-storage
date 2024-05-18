#!/usr/bin/env python3
"""All"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    return mongo_collection.find()
