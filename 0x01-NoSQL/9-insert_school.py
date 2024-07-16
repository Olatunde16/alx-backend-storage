#!/usr/bin/env python3
'''Task 9's module.
'''


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection object from pymongo.
    **kwargs: Arbitrary keyword arguments representing the document fields and values.

    Returns:
    ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
