from dataclasses import dataclass
from api.schemas.cart_product_schema import CartProduct

@dataclass
class Cart:
    userId:int
    date:str
    products:list[CartProduct]

    def to_dict(self):
        return {
            "userId": self.userId,
            "date": self.date,
            "products": [p.to_dict() for p in self.products]
        }