from dataclasses import dataclass

from homework_8.accessories.accessory import Accessory


@dataclass(frozen=True)
class Card(Accessory):
    text: str

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.text.strip():
            raise ValueError("Текст открытки не может быть пустым")
