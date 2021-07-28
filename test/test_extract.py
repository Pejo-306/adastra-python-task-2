import os
from unittest import TestCase

from src.definitions import TEST_INPUT_FILES_DIR
from src.extract import *


class TestExtractFunctions(TestCase):

    def test_extract_from_csv(self):
        input_filepath = os.path.join(TEST_INPUT_FILES_DIR, 'example_input.csv')
        data = extract_from_csv(input_filepath)
        self.assertIsInstance(data, list)
        # Examine first record
        self.assertIsInstance(data[0], dict)
        self.assertEqual('Sofia', data[0]['city'])
        self.assertEqual(' 2021-08-01T13:00:00+02:00', data[0]['date'])
        self.assertEqual(' 33C', data[0]['temp'])
        # Examine second record
        self.assertIsInstance(data[1], dict)
        self.assertEqual('Varna', data[1]['city'])
        self.assertEqual(' 2021-08-01T11:45:00Z', data[1]['date'])
        self.assertEqual('25 C', data[1]['temp'])

    def test_extract_from_json(self):
        input_filepath = os.path.join(TEST_INPUT_FILES_DIR, 'example_input.json')
        data = extract_from_json(input_filepath)
        self.assertIsInstance(data, list)
        # Examine first record
        self.assertIsInstance(data[0], dict)
        self.assertEqual('Sofia', data[0]['city'])
        self.assertEqual('2021-08-01T13:00:00+02:00', data[0]['date'])
        self.assertEqual(' 33C', data[0]['temp'])
        # Examine second record
        self.assertIsInstance(data[1], dict)
        self.assertEqual('Varna', data[1]['city'])
        self.assertEqual('2021-08-01T11:45:00Z', data[1]['date'])
        self.assertEqual('25 C', data[1]['temp'])
