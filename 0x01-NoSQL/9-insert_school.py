#!/usr/bin/env python3
"""Defines the function inserted_school"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
