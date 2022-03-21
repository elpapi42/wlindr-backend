from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Client():
    id: int
    name: str

@dataclass
class Product():
    id: int
    name: str
    price: float

@dataclass
class Basket():
    products: List[Product]

    def add(self, product: Product):
        self.products.append(product)

    def remove(self, product: Product):
        self.products.remove(product)

    def clear(self):
        self.products = []

    @property
    def price(self) -> float:
        return sum([product.price for product in self.products])

@dataclass
class Order():
    client: Client
    basket: Basket
    created_at: datetime
    fulfilled: bool = False
