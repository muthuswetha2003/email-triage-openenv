from pydantic import BaseModel
class Observation(BaseModel):
    query: str
class Action(BaseModel):
    response: str
