from enum import Enum


class StatusEnum(Enum):
    NORMAL = ("", "")
    BURN = ("Burn", "🔥")
    FREEZE = ("Freeze", "❄️")
    PARALYSIS = ("Paralysis", "⚡")
    POISON = ("Poison", "☠️")
    SLEEP = ("Sleep", "💤")

    def __init__(self, status, sprite_url):
        self.status = status
        self.sprite_url = sprite_url
