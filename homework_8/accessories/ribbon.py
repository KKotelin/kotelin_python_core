from dataclasses import dataclass

from homework_8.accessories.accessory import Accessory


@dataclass(frozen=True)
class Ribbon(Accessory):
    color: str

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.color.strip():
            raise ValueError("Цвет ленты не может быть пустым")
