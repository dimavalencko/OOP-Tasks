class TimeDeposit:
    def __init__(self, name, interest_rate, period_limit, sum_limit):
        self.name = name
        self._interest_rate = interest_rate
        self._period_limit = period_limit
        self._sum_limit = sum_limit

        self._check_self()

    def __str__(self):
        return f'Наименование:       {self.name}\n' \
               f'Валюта:             {self.currency}\n' \
               f'Процентная ставка:  {self._interest_rate}\n' \
               f'Срок (мес.):        [{self._period_limit[0]}; {self._period_limit[1]})\n' \
               f'Сумма:              [{self._sum_limit[0]}; {self._sum_limit[1]})'

    @property
    def currency(self):
        return "руб."

    def _check_self(self):
        assert 0 < self._interest_rate <= 100, \
            "Неверно указан процент по вкладу!"
        assert 1 <= self._period_limit[0] < self._period_limit[1], \
            "Неверно указаны ограничения по сроку вклада!"
        assert 0 < self._sum_limit[0] <= self._sum_limit[1], \
            "Неверно указаны ограничения по сумме вклада!"

    def _check_user_params(self, initial_sum, period):
        is_sum_ok = self._sum_limit[0] <= initial_sum < self._sum_limit[1]
        is_period_ok = self._period_limit[0] <= period < self._period_limit[1]
        assert is_sum_ok and is_period_ok, "Условия вклада не соблюдены!"

    def get_profit(self, initial_sum, period):
        self._check_user_params(initial_sum, period)
        return initial_sum * self._interest_rate / 100 * period / 12

    def get_sum(self, initial_sum, period):
        return initial_sum + self.get_profit(initial_sum, period)


class BonusTimeDeposit(TimeDeposit):
    def __init__(self, name, interest_rate, period_limit, sum_limit, bonus):
        self._bonus = bonus

        super().__init__(name, interest_rate, period_limit, sum_limit)

    def __str__(self):
        return super().__str__() + f'\nБонус (мин. сумма): {self._bonus["sum"]:.2f}'

    def _check_self(self):
        assert sorted(self._bonus.keys()) == ['percent', 'sum'], \
            'Неверно указан бонус по вкладу'
        assert isinstance(self._bonus['sum'], (int, float)), \
            'Неверно указан бонус по вкладу'
        assert isinstance(self._bonus['percent'], int), \
            'Неверно указан бонус по вкладу'
        super()._check_self()

    def get_profit(self, initial_sum, period):
        profit = super().get_profit(initial_sum, period)
        if initial_sum > self._bonus['sum']:
            profit *= 1 + self._bonus['percent'] / 100

        return profit


class CompoundTimeDeposit(TimeDeposit):

    def __str__(self):
        return super().__str__() + f'\nКапитализация %   : Да'

    def get_profit(self, initial_sum, period):
        super()._check_user_params(initial_sum, period)
        return initial_sum * (1 + self._interest_rate / 100 / 12) ** period - initial_sum


deposits_data = dict(interest_rate=5, period_limit=(6, 18),
                     sum_limit=(1000, 100000))

deposits = (
    TimeDeposit("Сохраняй", interest_rate=5,
                period_limit=(6, 18),
                sum_limit=(1000, 100000)),
    BonusTimeDeposit("Бонусный 2", **deposits_data,
                     bonus=dict(percent=5, sum=2000)),
    CompoundTimeDeposit("С капитализацией", **deposits_data)
)

