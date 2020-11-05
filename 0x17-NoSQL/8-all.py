#!/usr/bin/env python3
""" all """
import pymongo


def list_all(mongo_collection):
    """lists all documents in Python"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
