from unittest import TestCase

from src.transform import *


class TestTransformFunctions(TestCase):
    def test_to_fahrenheit_with_celsius_inputs(self):
        self.assertEqual('91 F', to_fahrenheit('33 C'))
        self.assertEqual('59 F', to_fahrenheit('15C'))
        self.assertEqual('10 F', to_fahrenheit('-12 C'))
        self.assertEqual('-40 F', to_fahrenheit('-40 C'))

    def test_to_fahrenheit_with_fahrenheit_inputs(self):
        self.assertEqual('59 F', to_fahrenheit('59F'))
        self.assertEqual('91 F', to_fahrenheit('91 F'))
        self.assertEqual('-40 F', to_fahrenheit('-40 F'))
