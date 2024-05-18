#!/usr/bin/env python3
"""All"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    schools = mongo_collection.find()
    if mongo_collection.count_documents({}) == 0:
        return []
    return schools
