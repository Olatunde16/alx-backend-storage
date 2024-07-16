#!/usr/bin/env python3
'''Task 10's module.
'''


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection object from pymongo.
    name (str): The name of the school to update.
    topics (list of str): The list of topics to set for the school.

    Returns:
    UpdateResult: The result of the update operation.
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
