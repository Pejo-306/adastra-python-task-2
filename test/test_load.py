import os
import filecmp
from datetime import datetime
from unittest import TestCase

from src.definitions import OUTPUT_DIR, TEST_INPUT_FILES_DIR
from src.load import *


class TestLoadFunctions(TestCase):

    def setUp(self) -> None:
        self.output_data = [
            {'city': 'Sofia', 'date': '2021-08-01T13:00:00+02:00', 'temp': '33C'},
            {'city': 'Varna', 'date': '2021-08-01T11:45:00Z', 'temp': '25 F'}
        ]

    def test_save_to_csv(self):
        output_filepath = os.path.join(OUTPUT_DIR, f'test_output_{datetime.now().strftime("%Y-%m-%d %H.%M.%S.%f")}.csv')
        gold_output_filepath = os.path.join(TEST_INPUT_FILES_DIR, 'gold_output.csv')
        try:
            load_as_csv(self.output_data, output_filepath)
            self.assertTrue(os.path.exists(output_filepath), "Output file was not created")
            self.assertTrue(filecmp.cmp(gold_output_filepath, output_filepath), "Output file does not contain valid source data")
        finally:
            os.remove(output_filepath)

    def test_save_to_json(self):
        output_filepath = os.path.join(OUTPUT_DIR, f'test_output_{datetime.now().strftime("%Y-%m-%d %H.%M.%S.%f")}.json')
        gold_output_filepath = os.path.join(TEST_INPUT_FILES_DIR, 'gold_output.json')
        try:
            load_as_json(self.output_data, output_filepath)
            self.assertTrue(os.path.exists(output_filepath), "Output file was not created")
            self.assertTrue(filecmp.cmp(gold_output_filepath, output_filepath), "Output file does not contain valid source data")
        finally:
            os.remove(output_filepath)
