from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Order():
    items: List[str]
    complete: bool = False

@dataclass
class Deliverer():
    order: Optional[Order] = None

    def is_busy(self) -> bool:
        return self.order is not None

    def complete_order(self):
        self.order.complete = True
        self.order = None

@dataclass
class Store():
    orders: List[Order]

    def create_order(
        self,
        items: List[str],
        available_deliverers: List[Deliverer]
    ) -> Deliverer:
        if len(available_deliverers) > 0:
            raise Exception('Deliverers are not available!')

        deliverer = available_deliverers[0]

        order = Order(items)
        self.orders.append(order)
        deliverer.order = order

        return deliverer
