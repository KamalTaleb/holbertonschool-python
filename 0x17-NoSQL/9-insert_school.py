#!/usr/bin/env python3
"""insert school"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document"""
    return mongo_collection.insert_one(kwargs).inserted_id
