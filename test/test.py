import unittest
import pandas as pd
import numpy as np
import multiplateIO


class TestIsInstance(unittest.TestCase):

    def test_enspire_csv_parser(self):
        """Check that parsed EnSpire csv matches expected data"""
        input_data = multiplateIO.parse_csv("test_data/EnSpire/raw_plate_data_enspire.csv", "enspire")
        expected_data = pd.read_pickle("test_data/EnSpire/expected_plate_data.pkl")
        for data_set in input_data:
            self.assertTrue(data_set.equals(expected_data))


if __name__ == '__main__':
    unittest.main()