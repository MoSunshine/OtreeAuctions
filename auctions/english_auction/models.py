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
    name_in_url = 'english_auction'
    players_per_group = None
    num_rounds = 100
    start_value = 200
    end_value= 100
    intervall_down = 1
    time_per_bet_in_seconds = 10

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
        minimum = Constants.start_value - Constants.end_value
        maximum = Constants.start_value
        estimate = random.randrange(minimum, maximum,Constants.intervall_down)
        return estimate

