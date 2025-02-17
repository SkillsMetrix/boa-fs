from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    uname: str
    email: str
    isJoined: bool =True
    rating: Optional[int] = None 
