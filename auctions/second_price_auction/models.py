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

import random

author = 'Moritz Wegener & Jeffrey Starck'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'second_price_auction'
    players_per_group = None
    num_rounds = 100
    endowment = c(100)
    value = c(150)
    error = c(50)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_winner = models.BooleanField(
        initial=False
    )
    winning_price = models.CurrencyField();
    cost = models.CurrencyField()
    bot_bid = models.CurrencyField()
    zero = models.CurrencyField()
    bid = models.CurrencyField(
        label="Please enter your bid.",
        min=0)

    def random_valuation(self):
        import random
        minimum = Constants.value - Constants.error
        maximum = Constants.value + Constants.error
        estimate = random.uniform(minimum, maximum)
        return estimate
    


        
        
        
        
