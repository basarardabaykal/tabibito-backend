from dataclasses import dataclass
from typing import Optional


@dataclass
class DetailedResult[T]:
    is_successful: bool
    message: str
    data: Optional[T] = None
