#!/usr/bin/env python3
'''Task 11's module.
'''


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection object from pymongo.
    topic (str): The topic to search for.

    Returns:
    list: A list of schools (documents) that include the specified topic.
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
