#!/usr/bin/env python3

def top_students(mongo_collection):
    """returns all students sorted by average score"""
    return mongo_collection.update_many({}, {'averageScore': {'$avg': '$topics.score'}})
