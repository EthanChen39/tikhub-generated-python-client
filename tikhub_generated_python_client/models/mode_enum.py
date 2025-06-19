from enum import Enum


class ModeEnum(str, Enum):
    DECRYPT = "decrypt"
    ENCRYPT = "encrypt"

    def __str__(self) -> str:
        return str(self.value)
