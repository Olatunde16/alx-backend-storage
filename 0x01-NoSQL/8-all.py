#!/usr/bin/env python3
'''Task 8's module.
'''

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection object from pymongo.

    Returns:
    list: A list of documents, or an empty list if no documents are found.
    """
    return [doc for doc in mongo_collection.find()]
