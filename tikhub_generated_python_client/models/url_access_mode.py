from enum import Enum


class UrlAccessMode(str, Enum):
    BLOCKED = "blocked"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
