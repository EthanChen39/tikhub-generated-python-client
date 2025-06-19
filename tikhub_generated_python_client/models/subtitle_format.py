from enum import Enum


class SubtitleFormat(str, Enum):
    SRT = "srt"
    TXT = "txt"
    VTT = "vtt"
    XML = "xml"

    def __str__(self) -> str:
        return str(self.value)
