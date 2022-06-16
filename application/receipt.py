

class Receipt:
    def __init__(self):
        self.__item_list_after_processing = list()
        self.__total_cost_with_taxes: float = 0.0
        self.__total_tax: float = 0.0

    def generate_receipt(self, items):
        for item in items:
            tax = item.get_tax()
            value_after_tax = item.get_value_after_tax()

            self.__total_cost_with_taxes += value_after_tax
            self.__total_tax += tax

            self.__item_list_after_processing.append(
                {
                    "itemName": item.get_item_name(),
                    "quantity": item.get_quantity(),
                    "valueAfterTax": value_after_tax
                }
            )

        return {
            "items": self.__item_list_after_processing,
            "totalCostWithTaxes": round(self.__total_cost_with_taxes, 2),
            "totalTax": round(self.__total_tax,2)
        }