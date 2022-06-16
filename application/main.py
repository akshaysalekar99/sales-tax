from receipt import Receipt
from item import Item
from utils import validate_input


def process_items(items_data):
    if not items_data:
        return None

    valid_flag, message = validate_input(items_data)

    if not valid_flag:
        return message

    item_objects = list()

    for product in items_data:
        new_item = Item(product)
        item_objects.append(new_item)

    new_receipt = Receipt()
    receipt_data = new_receipt.generate_receipt(item_objects)

    return receipt_data


if __name__ == "__main__":
    import sys
    import json

    args = sys.argv
    request_body = json.loads(args[1])
    response = process_items(request_body)
    print(json.dumps(response))


