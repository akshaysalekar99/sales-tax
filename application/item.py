from utils import round_up

ITEM_CATEGORY_DB = {
    "book": "book",
    "chocolates": "food",
    "headache pills": "medicine"
}


SALES_TAX_EXEMPT = ["book", "food", "medicine"]


class Item:

    def __init__(self, item_particulars: dict):
        self.__item_name: str = item_particulars.get("itemName", "")
        self.__quantity: int = item_particulars.get("quantity", 0)
        self.__value_before_tax: float = item_particulars.get("valueBeforeTax", 0.0)
        self.__is_imported: bool = item_particulars.get("isImported", False)
        self.__item_category: str = ITEM_CATEGORY_DB.get(self.__item_name, "")
        self.__tax: float = 0.0
        self.__is_tax_calculated: bool = False
        self.__sales_tax_rate: int = 10
        self.__import_tax_rate: int = 5

    def get_item_name(self):
        return self.__item_name

    def get_quantity(self):
        return self.__quantity

    def __calculate_tax(self):
        tax = 0.0
        if self.is_sale_tax_exempt() and not self.__is_imported:
            tax = 0.0

        elif self.is_sale_tax_exempt() and self.__is_imported:
            tax = self.__value_before_tax * (self.__import_tax_rate/100)

        elif not self.is_sale_tax_exempt() and self.__is_imported:
            tax = self.__value_before_tax * (self.__sales_tax_rate/100) + \
                  self.__value_before_tax * (self.__import_tax_rate/100)

        elif not self.is_sale_tax_exempt() and not self.__is_imported:
            tax = self.__value_before_tax * (self.__sales_tax_rate / 100)

        self.__tax = round_up(tax)
        self.__is_tax_calculated = True
        return self.__tax

    def is_sale_tax_exempt(self):
        return self.__item_category in SALES_TAX_EXEMPT

    def get_tax(self):
        if self.__is_tax_calculated:
            return self.__tax
        self.__calculate_tax()
        return self.__tax

    def get_value_after_tax(self):
        if not self.__is_tax_calculated:
            self.__calculate_tax()

        return round(self.__value_before_tax + self.__tax, 2)
