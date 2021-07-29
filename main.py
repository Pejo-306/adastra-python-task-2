import re
import logging

from src.extract import extract_from_csv, extract_from_json
from src.transform import to_fahrenheit
from src.load import load_as_csv, load_as_json


def main() -> None:
    # setup logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("(%(levelname)s) %(asctime)s: %(message)s")
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    csv_ext_pattern = re.compile(r'.*\.(csv)')
    json_ext_pattern = re.compile(r'.*\.(json)')
    input_filepath = input("Enter input filepath: ")
    output_filepath = input("Enter output filepath: ")

    # Extract the source data from the input
    logger.info("Extracting source data...")
    if csv_ext_pattern.match(input_filepath):
        data = extract_from_csv(input_filepath)
    elif json_ext_pattern.match(input_filepath):
        data = extract_from_json(input_filepath)
    else:
        raise ValueError("Input file must be either in CSV or JSON format")
    logger.info("Data extraction complete.")

    # Convert celsius temperature to fahrenheit
    logger.info("Transforming data...")
    for record in data:
        record['temp'] = to_fahrenheit(record['temp'])

    # Load transformed data to data sink
    logger.info("Loading data into sink...")
    if csv_ext_pattern.match(output_filepath):
        load_as_csv(data, output_filepath)
    elif json_ext_pattern.match(output_filepath):
        load_as_json(data, output_filepath)
    else:
        raise ValueError("Output file must be either in CSV or JSON format")
    logger.info("Data loading complete.")


if __name__ == '__main__':
    main()
