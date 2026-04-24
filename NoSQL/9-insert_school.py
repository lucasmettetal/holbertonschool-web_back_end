#!/usr/bin/env python3
"""Insert a document in a MongoDB collection"""
from typing import Any


def insert_school(mongo_collection: Any, **kwargs):
    """Insert a new document and return its _id."""
    return mongo_collection.insert_one(kwargs).inserted_id
