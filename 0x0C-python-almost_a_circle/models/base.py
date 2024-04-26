#!/usr/bin/python3

""" Modules for base.py """
from .base import Base

import json

if __name__ == "__main__":
    with open("base_data.json") as f:
        data = json.load(f)
        obj = Base(**data)
        print(obj.id)
