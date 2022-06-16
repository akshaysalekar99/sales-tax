import unittest
from receipt import Receipt as target
from item import Item


class TestReceipt(unittest.TestCase):
    def test_no_tax(self):
        req = [{"itemName": "book", "quantity": 1, "valueBeforeTax": 12.49},
               {"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 0.85},
               {"itemName": "headache pills", "quantity": 1, "valueBeforeTax": 9.75}]
        objs = [Item(product) for product in req]
        new_receipt = target().generate_receipt(objs)
        expected = {'items': [{'itemName': 'book', 'quantity': 1, 'valueAfterTax': 12.49},
                              {'itemName': 'chocolates', 'quantity': 1, 'valueAfterTax': 0.85},
                              {'itemName': 'headache pills', 'quantity': 1, 'valueAfterTax': 9.75}],
                    'totalCostWithTaxes': 23.09,
                    'totalTax': 0.0}
        self.assertEqual(new_receipt, expected)

    def test_all_tax_brackets(self):
        req = [{"itemName": "book", "quantity": 1, "valueBeforeTax": 12.49},
               {"itemName": "perfume", "quantity": 1, "valueBeforeTax": 18.99},
               {"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 11.25, "isImported": True},
               {"itemName": "perfume", "quantity": 1, "valueBeforeTax": 47.50, "isImported": True}]
        objs = [Item(product) for product in req]
        new_receipt = target().generate_receipt(objs)
        expected = {'items': [{'itemName': 'book', 'quantity': 1, 'valueAfterTax': 12.49},
                              {'itemName': 'perfume', 'quantity': 1, 'valueAfterTax': 20.89},
                              {'itemName': 'chocolates', 'quantity': 1, 'valueAfterTax': 11.85},
                              {'itemName': 'perfume', 'quantity': 1, 'valueAfterTax': 54.65}],
                    'totalCostWithTaxes': 99.88,
                    'totalTax': 9.65}
        self.assertEqual(new_receipt, expected)


if __name__ == '__main__':
    unittest.main()
