class TooLowPriceException(Exception):
    def __init__(self, purchase_price, retail_price):
        self.purchase_price = purchase_price
        self.retail_price = retail_price

    @property
    def get_purchase_price(self):
        return self.purchase_price

    @property
    def get_retail_price(self):
        return self.retail_price
