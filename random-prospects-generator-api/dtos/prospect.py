from pydantic import BaseModel

class Prospect(BaseModel):
    name: str
    mail: str
    phone_number: str
