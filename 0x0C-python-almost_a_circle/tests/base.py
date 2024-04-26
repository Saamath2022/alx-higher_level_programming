#!/usr/bin/python3

""" Module for base.py """
import json
from models.base import Base

if __name__ == "__main__":
    with open("base_data.json") as f:
        data = json.load(f)
        obj = Base(**data)
        print(obj.id)
