from homework_8.accessories.accessory import Accessory
from homework_8.flowers.flower import Flower


class Bouquet:
    def __init__(self) -> None:
        self._flowers: list[Flower] = []
        self._accessories: list[Accessory] = []

    @property
    def flowers(self) -> list[Flower]:
        return self._flowers.copy()

    @property
    def accessories(self) -> list[Accessory]:
        return self._accessories.copy()

    def add_flower(self, flower: Flower) -> None:
        if not isinstance(flower, Flower):
            raise TypeError("Недопустимый тип для добавления в букет")

        self._flowers.append(flower)

    def add_accessory(self, accessory: Accessory) -> None:
        if not isinstance(accessory, Accessory):
            raise TypeError("Недопустимый тип для добавления в букет")

        self._accessories.append(accessory)

    def total_price(self) -> float:
        flowers_price = sum(
            (flower.price for flower in self._flowers), 0.0
        )
        accessories_price = sum(
            (accessory.price for accessory in self._accessories), 0.0
        )

        return flowers_price + accessories_price

    def average_lifespan(self) -> float | None:
        if not self._flowers:
            return None

        total_lifespan = sum(flower.lifespan for flower in self._flowers)
        return total_lifespan / len(self._flowers)

    def sort_flowers_by_price(self, reverse: bool = False) -> None:
        self._flowers.sort(key=lambda flower: flower.price, reverse=reverse)

    def has_flower(self, flower: Flower) -> bool:
        return flower in self._flowers
