from dataclasses import dataclass


@dataclass(frozen=True)
class Accessory:
    price: float

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Стоимость не может быть отрицательной")
