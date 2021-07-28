import csv
import json
from typing import List, Dict


def load_as_csv(data: List[Dict[str, str]], filepath: str) -> None:
    with open(filepath, 'w+', newline='') as file:
        writer = csv.writer(file)
        for record in data:
            writer.writerow([record['city'], record['date'], record['temp']])


def load_as_json(data: List[Dict[str, str]], filepath: str) -> None:
    with open(filepath, 'w+') as file:
        json.dump(data, file)
