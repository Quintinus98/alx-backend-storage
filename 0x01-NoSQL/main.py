#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
import datetime

list_all = __import__("8-all").list_all

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    school_collection = client.my_db.school
    new_posts = [
        {
            "name": "Mike",
            "text": "Another post!",
            "tags": ["bulk", "insert"],
            "date": datetime.datetime(2009, 11, 12, 11, 14),
        },
        {
            "name": "Eliot",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45),
        },
    ]
    result = school_collection.insert_many(new_posts)
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get("_id"), school.get("name")))
