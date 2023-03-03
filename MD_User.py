from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum
from typing import Optional, List


class Gender(str, Enum):
    male = "Male"
    female = "Female"


class Role(str, Enum):
    user = "User"
    admin = "Admin"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    empid: str
    emailid: str
    mobile: str
    gender: Gender
    role: List[Role]


class UpdateUser(BaseModel):
    name: Optional[str]
    empid: Optional[str]
    emailid: Optional[str]
    mobile: Optional[str]
    gender: Optional[str]
    role: Optional[List[Role]]

class Scanneduser(BaseModel):
    name: Optional[str]
    empid: Optional[str]
    date: Optional[str]


