import unittest
import csv
import json
import os

class TestCSVtoJSON(unittest.TestCase):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # tests folder
    csv_path = os.path.join(BASE_DIR, '..', 'profiles1.csv')
    json_path = os.path.join(BASE_DIR, '..', 'data.json')

    def test_csv_has_12_columns(self):
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(len(header), 12, "CSV does not have 12 columns")

    def test_csv_has_more_than_900_rows(self):
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertGreater(len(rows) - 1, 900, "CSV does not have more than 900 rows")

    def test_json_has_more_than_900_items(self):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.assertGreater(len(data), 900, "JSON does not have more than 900 items")

    def test_json_properties_are_complete(self):
        expected_keys = [
            "Givenname", "Surname", "Streetaddress", "City", "Zipcode",
            "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"
        ]
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                self.assertEqual(set(item.keys()), set(expected_keys), "JSON is missing expected keys")

    def test_always_pass(self):
        self.assertEqual(1 + 1, 2, "This test should always pass")

if __name__ == '__main__':
    unittest.main()

