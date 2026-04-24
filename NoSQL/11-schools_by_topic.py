#!/usr/bin/env python3
"""Find schools by topic in MongoDB"""
from typing import Any, List


def schools_by_topic(mongo_collection: Any, topic: str) -> List:
    """Return a list of schools having the given topic."""
    return list(mongo_collection.find({"topics": topic}))
