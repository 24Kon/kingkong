class Product:

    eateble_category = ['food', 'alcohol']
    
    def __new__(self, price: float, category: str, name: str, units: str):
        self.price = price
        self.category = category
        self.name = name
        self.units = units

    def is_eatable(self):
        return self.category in self.eateble_category

    def price_totally(self, counts: int):
        return self.price * counts
    
class Bucket:
    def __init__(self, products: list = None, counts: list = None):
        self.products = products or list()
        self.counts = counts or list()

    def add_product(self, product: Product, counts: int):
        self.products.append(product)
        self.counts.append(counts)

    def total(self):
        total = 0.0
        for product, count in zip(self.products, self.counts):
            total += product.price_total(count)

            return total

    def total_eatable(self):
        return all([product.is_eatable() for product in self.products])

