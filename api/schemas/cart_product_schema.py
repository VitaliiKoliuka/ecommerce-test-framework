
from dataclasses import dataclass

@dataclass
class CartProduct:
    productId:int
    quantity:int

    def to_dict(self):
        return {
            "id": self.productId,
            "quantity": self.quantity
        }
