#!/usr/bin/env python3
"""Update topics of a school document in MongoDB"""
from typing import Any, List


def update_topics(mongo_collection: Any, name: str, topics: List[str]):
    """Update all topics of a school document matching the given name."""
    mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
