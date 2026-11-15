from homework_8.accessories.card import Card
from homework_8.accessories.ribbon import Ribbon
from homework_8.bouquet import Bouquet
from homework_8.flowers.rose import Rose
from homework_8.flowers.tulip import Tulip

if __name__ == '__main__':
    rose = Rose(price=150.0, lifespan=7)
    tulip = Tulip(price=100.0, lifespan=5)
    ribbon = Ribbon(price=50.0, color="Красный")
    card = Card(price=10.0, text="С др")

    bouquet = Bouquet()
    bouquet.add_flower(rose)
    bouquet.add_flower(tulip)
    bouquet.add_accessory(ribbon)
    bouquet.add_accessory(card)

    print(bouquet.total_price())
    print(bouquet.average_lifespan())
    print(bouquet.has_flower(rose))

    bouquet.sort_flowers_by_price()
    print(bouquet.flowers)
