from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Client():
    id: int
    name: str

@dataclass
class Item():
    id: int
    name: str
    price: float

@dataclass
class Basket():
    items: List[Item]

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def clear(self):
        self.items = []

    @property
    def price(self) -> float:
        return sum([item.price for item in self.items])

@dataclass
class Order():
    client: Client
    basket: Basket
    created_at: datetime
    fulfilled: bool = False
