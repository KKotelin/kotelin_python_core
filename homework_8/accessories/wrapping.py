from dataclasses import dataclass

from homework_8.accessories.accessory import Accessory


@dataclass(frozen=True)
class Wrapping(Accessory):
    material: str

    def __post_init__(self) -> None:
        super().__post_init__()
        if not self.material.strip():
            raise ValueError("Материал упаковки не может быть пустым")
