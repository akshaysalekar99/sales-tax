import unittest
from main import process_items


class TestMain(unittest.TestCase):
    def test_empty(self):
        request = []
        response = process_items(request)
        expected = None
        self.assertEqual(response, expected)

    def test_invalid_input_missing_key(self):
        request = [{"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 10.00, "isImported": True},
                   {"quantity": 1, "valueBeforeTax": 10.00, "isImported": True}]
        response = process_items(request)
        expected = "Invalid Input: itemName is a mandatory field"
        self.assertEqual(response, expected)

    def test_invalid_input_misspelled_key(self):
        request = [{"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 10.00, "isImported": True},
                   {"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 10.00, "is_Imported": True}]
        response = process_items(request)
        expected = "Invalid Input: is_Imported is not a supported field."
        self.assertEqual(response, expected)

    def test_valid_input(self):
        request = [{"itemName": "book", "quantity": 1, "valueBeforeTax": 12.49},
                   {"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 0.85},
                   {"itemName": "headache pills", "quantity": 1, "valueBeforeTax": 9.75}]
        response = process_items(request)
        expected = {'items': [{'itemName': 'book', 'quantity': 1, 'valueAfterTax': 12.49},
                              {'itemName': 'chocolates', 'quantity': 1, 'valueAfterTax': 0.85},
                              {'itemName': 'headache pills', 'quantity': 1, 'valueAfterTax': 9.75}],
                    'totalCostWithTaxes': 23.09,
                    'totalTax': 0.0}
        self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
