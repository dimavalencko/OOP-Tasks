from pizza import *

class Order:
    orderCounter = 0
    
    def __init__(self): 
        self.orderedPizzas = []
        Order.orderCounter += 1
        self.orderNumber = Order.orderCounter
        
    def __str__(self):
        result = (
            f'Заказ №{self.orderNumber}\n' + 
            '\n'.join([f'{i + 1}. ' + str(pizza) for i, pizza in enumerate(self.orderedPizzas)]))
        return result
    
    def addPizzaToOrder(self, pizza):
        self.orderedPizzas.append(pizza)
        
    def summ(self): 
        return sum(pizza.price for pizza in self.orderedPizzas)
    
    def completeOrder(self): 
        for i, pizza in enumerate(self.orderedPizzas, start=1):
            print(f'{i}. {pizza.name}')
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print(f'Заказ №{self.orderNumber} готов! Приятного аппетита!')
        