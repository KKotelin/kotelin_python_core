from dataclasses import dataclass


@dataclass(frozen=True)
class Flower:
    name: str
    price: float
    lifespan: int

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        if self.lifespan <= 0:
            raise ValueError("Время жизни должно быть положительным")
