#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB.
The format:
    x logs: where x is the number of documents in collection
    Methods:
        method y: z where y is the HTTP method and is the number of occurences
    w status check: w is the number of get methods with /status path
"""

import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient()
    db = client.logs
    collection = db.nginx
    stats = collection.aggregate(
        [
            {
                "$group": {"_id": "$method", "count": {"$sum": 1}}
            }
        ]
    )

    method_counts = {
        'GET': 0,
        'POST': 0,
        'PUT': 0,
        'PATCH': 0,
        'DELETE': 0,
    }

    total_logs = 0

    for stat in stats:
        if stat['_id'] in method_counts:
            method_counts[stat['_id']] = stat['count']
        total_logs += stat['count']

    status_check_counts = collection.count_documents({'path': '/status'})

    print("{} logs".format(total_logs))
    print("Methods:")
    for method, count in method_counts.items():
        print("    method {}: {}".format(method, count))
    print("{} status check".format(status_check_counts))
    client.close()
