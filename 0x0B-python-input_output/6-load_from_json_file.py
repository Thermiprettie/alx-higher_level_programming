#!/usr/bin/python3
"""Define function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """load the Object from JSON file."""
    with open(filename) as f:
        return json.load(f)
