#!/usr/bin/env python3
"""List all documents in a MongoDB collection"""
from typing import Any, List


def list_all(mongo_collection: Any) -> List:
    """Return a list of all documents in the collection."""
    return list(mongo_collection.find()) or []
