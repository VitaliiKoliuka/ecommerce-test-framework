from dataclasses import dataclass
from api.schemas.geolocation_schema import Geolocation

@dataclass
class Address:
   city: str
   street: str
   number: int
   zipcode: str
   geolocation: Geolocation