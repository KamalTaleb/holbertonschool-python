#!/usr/bin/env python3
"""update topics"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """changes school topics"""
    return mongo_collection.update_many({"name": name}, {
        "$set": {"topics": topics}})
