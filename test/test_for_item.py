import unittest
from item import Item as target


class TestItem(unittest.TestCase):
    def test_no_tax(self):
        request = {"itemName": "book", "quantity": 1, "valueBeforeTax": 12.49}
        response = target(request).get_tax()
        expected = 0.0
        self.assertEqual(response, expected, "Should be 0.0")

    def test_sales_tax_only(self):
        request = {"itemName": "Music CD", "quantity": 1, "valueBeforeTax": 14.99}
        response = target(request).get_tax()
        expected = 1.5
        self.assertEqual(response, expected, "Should be 1.5")

    def test_import_tax_only(self):
        request = {"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 10.00, "isImported": True}
        response = target(request).get_tax()
        expected = 0.5
        self.assertEqual(response, expected, "Should be 0.5")

    def test_both_sales_and_import_tax(self):
        request = {"itemName": "perfume", "quantity": 1, "valueBeforeTax": 27.99, "isImported": True}
        response = target(request).get_tax()
        expected = 4.2
        self.assertEqual(response, expected, "Should be 4.2")


if __name__ == '__main__':
    unittest.main()
