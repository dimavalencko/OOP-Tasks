class Pizza:
    def __init__(self):
        self.name = 'Заготовка'
        self.dough = 'тонкое'
        self.sauce = 'кетчуп'
        self.filling = []
        self.price = 0
        
    def __str__(self):
        return f'Пицца: {self.name} | Цена: {self.price:.2f} р.\n' \
               f'   Тесто: {self.dough} Соус: {self.sauce}\n' \
               f'   Начинка: {", ".join(self.filling)}'
               
    def prepare(self):
        print(
            f'Начинается процесс готовки пиццы {self.name}',
            f' - замешивается {self.dough} тесто',
            f' - добавляется соус: {self.sauce}',
            f' - добавляется начинка: {", ".join(self.filling)}',
            sep='\n'
        )
    
    def bake(self):
        print('Пицца печется')

    def cut(self):
        print('Пицца нарезается')

    def pack(self):
        print('Пицца упаковывается')
        
        
class PizzaPepperoni(Pizza):
    def __init__(self):
        super().__init__()

        self.name = 'Пипперони'
        self.sauce = 'томатный'
        self.daugh = 'тонкое'
        self.filling = [
            'томаты', 'колбаса салями', 'сыр моцарелла',
            'перец чили', 'чеснок', 'сушённый базелик',
            'оливковое масло'
        ]

        self.price = 550

class PizzaBarbecue(Pizza):
    def __init__(self):
        super().__init__()

        self.name = 'Барбекю'
        self.sauce = 'барбекю'
        self.daugh = 'тонкое'
        self.filling = [
            'томаты', 'говядина', 'сыр моцарелла',
            'баклажан', 'шампиньоны', 'лук сладкий',
            'солённый огурец'
        ]

        self.price = 625


class PizzaGiftsOfTheSea(Pizza):
    def __init__(self):
        super().__init__()

        self.name = 'Дары моря'
        self.sauce = 'чесночный'
        self.daugh = 'тонкое'
        self.filling = [
            'семга', 'креветки', 'сыр моцарелла',
            'мидии', 'маслины', 'лук красный'
        ]

        self.price = 700
