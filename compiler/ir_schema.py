from pydantic import BaseModel
from typing import List, Literal

class Scene(BaseModel):
    type: Literal["array", "compare", "swap"]
    i: int | None = None
    j: int | None = None
    values: List[int] | None = None

class VideoIR(BaseModel):
    topic: str
    scenes: List[Scene]