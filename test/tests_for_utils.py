import unittest
import utils as target


class TestRounding(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(target.round_up(0.0), 0.0, "Should be 0.0")

    def test_point_zero_one(self):
        self.assertEqual(target.round_up(0.01), 0.05, "Should be 0.05")

    def test_point_152(self):
        self.assertEqual(target.round_up(0.152), 0.2, "Should be 0.2")

    def test_point_five(self):
        self.assertEqual(target.round_up(0.5), 0.5, "Should be 0.5")

    def test_one(self):
        self.assertEqual(target.round_up(1.0), 1.0, "Should be 1.0")


class TestValidation(unittest.TestCase):

    def test_positive(self):
        request = [{"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 10.00, "isImported": True}]
        response = target.validate_input(request)
        expected = (True, "Valid Input")
        self.assertEqual(response, expected, "Should be True")

    def test_not_list(self):
        response = target.validate_input({})
        expected = (False, "Invalid Input: Should be a list")
        self.assertEqual(response, expected, "Should be False")

    def test_not_dict(self):
        response = target.validate_input([[]])
        expected = (False, "Invalid Input: Product should be a dictionary")
        self.assertEqual(response, expected, "nested value Should be a dictionary")

    def test_not_item_name(self):
        request = [{"quantity": 1, "valueBeforeTax": 10.00, "isImported": True}]
        response = target.validate_input(request)
        expected = (False, "Invalid Input: itemName is a mandatory field")
        self.assertEqual(response, expected, "Should be False")

    def test_value_less_than_eq_zero(self):
        request = [{"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 0.00, "isImported": True}]
        response = target.validate_input(request)
        expected = (False, "Invalid Input: valueBeforeTax cannot be less than or equal to zero.")
        self.assertEqual(response, expected, "Should be False")

    def test_quantity_int(self):
        request = [{"itemName": "chocolates", "quantity": "1", "valueBeforeTax": 10.00, "isImported": True}]
        response = target.validate_input(request)
        expected = False, "Invalid Input: quantity field is not of the expected type <class 'int'>"
        self.assertEqual(response, expected, "Should be False")


if __name__ == "__main__":
    unittest.main()
