from pydantic import BaseModel
from typing import Optional, Any

class UserCreate(BaseModel):
    email: str
    full_name: str
    password: str
    role: str
    department: Optional[str] = None

class FormCreate(BaseModel):
    department: str
    faculty: str
    category: str
    criterion: str
    data: Any
