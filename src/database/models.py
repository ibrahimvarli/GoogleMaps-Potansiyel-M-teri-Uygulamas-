from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Business:
    id: Optional[int]
    place_id: str
    name: str
    address: str
    phone: str
    category: str
    rating: float
    lat: float
    lng: float
    created_at: datetime = None

@dataclass
class Customer:
    id: Optional[int]
    name: str
    email: str
    phone: str
    address: str
    preferences: List[str]
    last_visit: Optional[datetime] = None
    created_at: datetime = None 