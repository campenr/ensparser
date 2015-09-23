import unittest

import os.path
import pandas as pd

from multiplate import multiplateIO

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")

class TestIsInstance(unittest.TestCase):

    def test_enspire_csv_parser(self):
        """Check that parsed EnSpire csv matches expected data"""
        test_dir = os.path.join(TEST_DATA_DIR, "EnSpire")
        input_data = multiplateIO.parse_csv(os.path.join(test_dir, "raw_plate_data_enspire.csv"), "enspire")
        expected_data = pd.read_pickle(os.path.join(test_dir, "expected_plate_data.pkl"))
        # input_data is an iterator with one item
        for data_set in input_data:
            self.assertTrue(data_set.equals(expected_data))


if __name__ == '__main__':
    unittest.main()