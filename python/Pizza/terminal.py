from pizza import *
from order import *


class Terminal:
    company = 'PizzasLab'
    orderCancellationCmd = -1
    orderConfirmCmd = 0
    version = 1.0

    def __init__(self):
        self.menu = [PizzaPepperoni(), PizzaBarbecue(), PizzaGiftsOfTheSea()]
        self.order = None
        self.isDisplayMenu = True

    def __str__(self):
        return f'{Terminal.company}, {Terminal.version}'

    def displayMenu(self):
        if not self.isDisplayMenu:
            return

        print(
            f'{Terminal.company}', 'Добро пожаловать!', '', 'Меню:',
            *[f'{i + 1}. ' + str(pizza) for i, pizza in enumerate(self.menu)],
            'Для выбора укажите цифру через <ENTER>.',
            'Для отмены заказа введите -1',
            'Для подтверждения заказа введите 0',
            sep='\n'
        )

        self.isDisplayMenu = False

    def processComand(self, menuItem):
        try:
            menuItem = int(menuItem)
            if menuItem == Terminal.orderCancellationCmd:
                self.order = None
                print('Ваш заказ отменён')
            elif menuItem == Terminal.orderConfirmCmd:
                if self.order is not None:
                    print('Заказ подтвержен.')
                    print(self.order)
                    self.acceptThePayment()
                    self.order.perform()
            elif 1 <= menuItem <= len(self.menu):
                if self.order is None:
                    self.order = Order()
                self.order.addPizzaToOrder(self.menu[menuItem - 1])
                print(f'Пицца {self.order.orderedPizzas[-1].name} добавлена!')
            else:
                raise ValueError
        except ValueError:
            print("Не могу распознать команду! Проверьте ввод.")
        except Exception as e:
            print("Во время работы терминала произошла ошибка...", e)

    def calculatePayoff(self, payment):
        if payment < self.order.summ():
            raise ValueError

        return payment - self.order.summ()

    def acceptThePayment(self):
        try:
            print(f'Сумма заказа: {self.order.summ():.2f}')
            payment = float(input('Введите сумму: '))
            change = self.calculatePayoff(payment)
            print(f'Вы внесли {payment:.2f} р. Сдача: {change:.2f} р.')
        except Exception:
            print("Оплата не удалась. Заказ будет отменен.")
            raise


