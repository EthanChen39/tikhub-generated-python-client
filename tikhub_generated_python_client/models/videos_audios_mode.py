from enum import Enum


class VideosAudiosMode(str, Enum):
    AUTO = "auto"
    FALSE = "false"
    RAW = "raw"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
