#!/usr/bin/env python3
"""Defines the function update_topics"""

def update_topics(mongo_collection, name, topics):
    """updates all topics of a school document based on the name"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
