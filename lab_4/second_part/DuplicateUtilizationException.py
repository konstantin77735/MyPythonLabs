class DuplicateUtilizationException(RuntimeError):
    def __init__(self, product):
        self.product = product
        self.name = None

    def get_product(self):
        return self.product

    def get_name(self):
        return self.name
