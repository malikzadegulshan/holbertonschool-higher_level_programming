#!/usr/bin/env python3
"""Module for converting CSV files to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and write the output to data.json.

    Returns True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            rows = list(csv.DictReader(csv_file))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
