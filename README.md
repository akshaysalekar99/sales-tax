# Sales Tax Assignment

___

### Directory Structure

- sales_tax/application/ contains the source code.
- sales_tax/test/ contains the unit tests.
- sales_tax/resources contains some input samples and output.


### Usage

1. Entry point is at sales_tax/application/main.py
2. To run the tests in sales_tax/test/, sales_tax/application/ will need to be marked as source root.
3. Input samples are from sales_tax/resources/samples.txt
4. Input is expected in the following format:


    "itemName": str,
    "quantity": int,
    "valueBeforeTax": float,
    "isImported": bool

5. Console usage.

```commandline
python3 main.py '[{"itemName": "chocolates", "quantity": 1, "valueBeforeTax": 10.00, "isImported": true}]'
```