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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Second_Price_Auction_Bots'
    players_per_group = None
    num_rounds = 5
    endowment = c(100)
    value = c(150)
    error = c(50)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    bot1 = models.CurrencyField()
    #bot2 = models.CurrencyField()
    
   # bot1 = models.CurrencyField(initial=c(random.uniform(Constants.value - Constants.error, Constants.value + Constants.error)))
   # bot2 = models.CurrencyField(initial=c(random.uniform(Constants.value - Constants.error, Constants.value + Constants.error)))
    #bot1 = random.uniform(Constants.value - Constants.error, Constants.value + Constants.error)
    #bot2 = random.uniform(Constants.value - Constants.error, Constants.value + Constants.error)
    bid = models.CurrencyField(
        label="What is your bid?",
        min=0)
    highest_bid = models.CurrencyField()
    second_highest_bid = models.CurrencyField()
    
    def highest(self):
        print(min([self.bid, self.bot1]))
        print(sorted([self.bid, self.bot1])[1])
        players = self.get_players()
        #print(self.get_players())
        #print(self.bid, Constants.bot1, Constants.bot2)
        self.highest_bid = min([self.bid, self.bot1])
        self.second_highest_bid = sorted([self.bid, self.bot1])[1]
        #return self.highest_bid
        #return self.second_highest_bid
        #player_with_highest_bid = [self.bid==self.highest_bid]
        #winner = random.choice(player_with_highest_bid)
        #winner.is_winner = True
      
        #if self.bid==self.highest_bid:
        #    self.group.player.is_winner=True
      
        for p in players:
            p.set_payoff()    
      #self.group.player.set_payoff()


class Player(BasePlayer):
    is_winner = models.BooleanField(
        initial = False
    )
    
    valuation = models.CurrencyField()
    profit = models.CurrencyField(initial=c(0))
    
    def random_valuation(self):
        import random
        minimum = Constants.value - Constants.error
        maximum = Constants.value + Constants.error
        estimate = random.uniform(minimum, maximum)
        return estimate
    
    def set_payoff(self):
        if self.group.bid==self.group.highest_bid:
            self.is_winner=True
        if self.is_winner:
            self.payoff = self.group.second_highest_bid - self.valuation
        else:
            self.payoff = c(0)
        
        if self.round_number==1:
            self.profit = self.payoff
        else:
            self.profit = self.in_round(self.round_number - 1).profit +  self.payoff 

        
        
        
        
        
