import math

mandatory_keys = ["itemName", "quantity", "valueBeforeTax"]
allowed_keys = ["itemName", "quantity", "valueBeforeTax", "isImported"]
type_mapping = {
    "itemName": str,
    "quantity": int,
    "valueBeforeTax": float,
    "isImported": bool
}


def validate_input(items_data):
    if not isinstance(items_data, list):
        return False, "Invalid Input: Should be a list"

    for product in items_data:
        if not isinstance(product, dict):
            return False, "Invalid Input: Product should be a dictionary"

        for key in mandatory_keys:
            if key not in product:
                return False, "Invalid Input: {} is a mandatory field".format(key)

        for key, val in product.items():
            if key not in type_mapping:
                return False, "Invalid Input: {} is not a supported field.".format(key)

            if type(val) != type_mapping[key]:
                return False, "Invalid Input: {} field is not of the expected type {}".format(key, type_mapping[key])

            if key == "quantity" and val < 1:
                return False, "Invalid Input: Quantity cannot be less than 1."

            if key == "valueBeforeTax" and val <= 0:
                return False, "Invalid Input: valueBeforeTax cannot be less than or equal to zero."

    return True, "Valid Input"


def round_up(num):
    if not num:
        return num
    round_to = 0.05
    rounded_tax = round(num / round_to) * round_to
    if math.isclose(num, rounded_tax):
        return num
    if rounded_tax > num:
        return round(rounded_tax, 2)
    else:
        rounded_tax += round_to
        return round(rounded_tax, 2)