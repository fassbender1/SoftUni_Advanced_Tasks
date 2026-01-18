from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PROD_TYPES = {"Chair": Chair,
                   "HobbyHorse": HobbyHorse
                   }

    VALID_STORE_TYPES = {"FurnitureStore": FurnitureStore,
                         "ToyStore": ToyStore
                         }

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float) -> str:
        if product_type not in self.VALID_PROD_TYPES:
            raise Exception("Invalid product type!")
        product = self.VALID_PROD_TYPES[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORE_TYPES:
            raise Exception(f"{store_type} is an invalid type of store!")
        store = self.VALID_STORE_TYPES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        filtered_products = [prod for prod in products if prod.sub_type.lower() in store.store_type.lower()]
        if not filtered_products:
            return f"Products do not match in type. Nothing sold."

        for prod in filtered_products:
            self.products.remove(prod)
            store.capacity -= 1
            store.products.append(prod)
            self.income += prod.price

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store = self.__find_store(store_name)
        if store is None:
            raise Exception("No such store!")
        if store.products:
            return f"The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        discounted_prods = [prod for prod in self.products if prod.model == product_model]
        for product in discounted_prods:
            product.discount()
        return f"Discount applied to {len(discounted_prods)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = self.__find_store(store_name)
        if store is None:
            return f"There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        products = {}
        total_price = 0
        for prod in self.products:
            products[prod.model] = products.get(prod.model, 0) + 1
            total_price += prod.price

        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}"
        ]

        for model in sorted(products.keys()):
            result.append(f"{model}: {products[model]}")

        result.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            result.append(store.name)
        return "\n".join(result).strip()


    def __find_store(self, name) -> BaseStore | None:
        return next((store for store in self.stores if store.name == name), None)





























































































