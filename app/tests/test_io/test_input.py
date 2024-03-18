import sys
from pathlib import Path
sys.path.append(str(Path(__file__).cwd().parent.parent.parent.absolute()))

import unittest

import pandas as pd

from app.io.input import read_from_file_builtin, read_from_file_pandas

class TestReadFileBuiltin(unittest.TestCase):

    def test_read_existing_file(self):
        filepath = "test_data/input.txt"
        expected_text = "Це приклад тексту з файлу."
        actual_text = read_from_file_builtin(filepath)
        self.assertEqual(expected_text, actual_text)

    def test_read_nonexistent_file(self):
        filepath = "test_data/nonexistent_file.txt"
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin(filepath)

    def test_read_empty_file(self):
        filepath = "test_data/empty_file.txt"
        expected_text = ""
        actual_text = read_from_file_builtin(filepath)
        self.assertEqual(expected_text, actual_text)


class TestReadFilePandas(unittest.TestCase):

    def test_read_existing_file(self):
        filepath = "test_data/input.csv"
        expected_text = ["Це", "приклад", "тексту", "0", "2", "3", "4", "1", "5", "6", "7"]
        actual_text = read_from_file_pandas(filepath).split()
        self.assertEqual(expected_text, actual_text)

    def test_read_nonexistent_file(self):
        filepath = "test_data/nonexistent_file.csv"
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas(filepath)

    def test_read_empty_file(self):
        filepath = "test_data/empty_file.csv"
        with self.assertRaises(pd.errors.EmptyDataError):
            read_from_file_pandas(filepath)

if __name__ == "__main__":
    unittest.main()
