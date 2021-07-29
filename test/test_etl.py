import os
import filecmp
from datetime import datetime
from unittest import TestCase

from src.definitions import TEST_INPUT_FILES_DIR, OUTPUT_DIR
from src.extract import extract_from_json
from src.transform import to_fahrenheit
from src.load import load_as_csv


class TestETLProcess(TestCase):

    def test_entire_etl(self):
        input_filepath = os.path.join(TEST_INPUT_FILES_DIR, 'example_input.json')
        output_filepath = os.path.join(OUTPUT_DIR, f'test_output_{datetime.now().strftime("%Y-%m-%d %H.%M.%S.%f")}.csv')
        gold_output_filepath = os.path.join(TEST_INPUT_FILES_DIR, 'gold_output_etl.csv')
        # read input data
        data = extract_from_json(input_filepath)
        # convert celsius to fahrenheit
        for record in data:
            record['temp'] = to_fahrenheit(record['temp'])
        # load to output
        try:
            load_as_csv(data, output_filepath)
            self.assertTrue(os.path.exists(output_filepath), "Output file was not created")
            self.assertTrue(filecmp.cmp(gold_output_filepath, output_filepath), "Output file does not contain valid source data")
        finally:
            os.remove(output_filepath)
