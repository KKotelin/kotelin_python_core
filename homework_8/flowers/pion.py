from dataclasses import dataclass

from homework_8.flowers.flower import Flower


@dataclass(frozen=True)
class Pion(Flower):
    def __init__(self, price: float, lifespan: int) -> None:
        super().__init__("Пион", price, lifespan)
