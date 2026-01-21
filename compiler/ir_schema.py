from pydantic import BaseModel
from typing import List, Literal

class VideoIR(BaseModel):
    topic: Literal["bubble_sort"]
    input: List[int]

