import unittest
from code.data import Data
import os.path
from config import *


class TestData(unittest.TestCase):
    def setUp(self):
        self.data_object = Data()

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(path_to_data_file))

    def test_number_of_entries(self):
        with open(path_to_data_file, 'rb') as data_file:
            file_lines_count = len(data_file.readlines())
            print(file_lines_count)
        self.assertTrue(file_lines_count == number_of_entries)

if __name__ == '__main__':
    unittest.main()
