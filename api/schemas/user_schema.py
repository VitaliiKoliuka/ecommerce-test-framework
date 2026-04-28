from dataclasses import dataclass
from api.schemas.name_schema import Name
from api.schemas.address_schema import Address

@dataclass
class User:
    email:str
    username:str
    password:str
    name:Name
    address:Address
    phone:str