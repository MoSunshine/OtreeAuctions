from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Moritz Wegener & Jeffrey Starck'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dutch_auction'
    players_per_group = None
    num_rounds = 100
    start_value = 100
    end_value = 200
    intervall_up = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    winning_price = models.CurrencyField();
    cost = models.CurrencyField()
    bot_stop = models.CurrencyField()

    def random_valuation(self):
        import random
        minimum = Constants.end_value - Constants.start_value
        maximum = Constants.end_value
        estimate = random.randrange(minimum, maximum, Constants.intervall_up)
        return estimate
