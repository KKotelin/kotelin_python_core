from homework_7.homework_7_1.credit_card import CreditCard

if __name__ == '__main__':
    card_1 = CreditCard("40817-1", 500)
    card_2 = CreditCard("40817-2", 1000)
    card_3 = CreditCard("40817-3", 2000)

    card_1.deposit(500)
    card_2.deposit(1000)
    card_3.withdraw(1000)

    card_1.show_info()
    card_2.show_info()
    card_3.show_info()