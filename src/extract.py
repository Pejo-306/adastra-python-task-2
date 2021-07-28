import csv
import json
from typing import List, Dict


def extract_from_csv(filepath: str) -> List[Dict[str, str]]:
    """Extract data records from a CSV file

    :param filepath: OS file path to source CSV file
    :type filepath: str
    :return: list of data records, stored as Python dictionaries
    :rtype: List[Dict[str, str]]
    """
    data = []
    with open(filepath, mode='r') as file:
        for record in csv.reader(file):
            data.append({'city': record[0], 'date': record[1], 'temp': record[2]})
    return data


def extract_from_json(filepath: str) -> List[Dict[str, str]]:
    """Extract data records from a JSON file

    :param filepath: OS file path to source JSON file
    :type filepath: str
    :return: list of data records, stored as Python dictionaries
    :rtype: List[Dict[str, str]]
    """
    with open(filepath, mode='r') as file:
        data = json.loads(file.read())
    return data
