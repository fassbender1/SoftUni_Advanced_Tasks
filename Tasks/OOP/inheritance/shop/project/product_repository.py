from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f'{prod.name}: {prod.quantity}' for prod in self.products])
