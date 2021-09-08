from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    def before_next_page(self):
        self.player.valuation = self.player.random_valuation()
        self.group.bot1 = self.player.random_valuation()
        #self.group.bot2 = self.player.random_valuation()
    
class Auction(Page):
    form_model = 'group'
    form_fields = ['bid']
   # def before_next_page(self):
   #     'highest'
        #self.group.highest()
    def vars_for_template(self):
        a = self.round_number
        return dict(a=a)
        

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'highest'
    #'highest'
    #def before_next_page(player):
        #"set_payoff"
        
    
class Results(Page):
    def vars_for_template(self):
        a = self.round_number
        
        bid1 = self.group.in_round(1).bid
        win1 = self.group.in_round(1).bot1
        price1 = self.group.in_round(1).second_highest_bid
        cost1 = self.player.in_round(1).valuation
        profit1 = self.player.in_round(1).payoff
        if self.player.in_round(1).is_winner==True:
            winner1 = "Yes"
        else:
            winner1 = "No"
        
        
        bid2 = self.group.in_round(2).bid
        win2 = self.group.in_round(2).bot1
        price2 = self.group.in_round(2).second_highest_bid
        cost2 = self.player.in_round(2).valuation
        profit2 = self.player.in_round(2).payoff
        if self.player.in_round(2).is_winner==True:
            winner2 = "Yes"
        else:
            winner2 = "No"
        
        bid3 = self.group.in_round(3).bid
        win3 = self.group.in_round(3).bot1
        price3 = self.group.in_round(3).second_highest_bid
        cost3 = self.player.in_round(3).valuation
        profit3 = self.player.in_round(3).payoff
        if self.player.in_round(3).is_winner==True:
            winner3 = "Yes"
        else:
            winner3 = "No"
        
        bid4 = self.group.in_round(4).bid
        win4 = self.group.in_round(4).bot1
        price4 = self.group.in_round(4).second_highest_bid
        cost4 = self.player.in_round(4).valuation
        profit4 = self.player.in_round(4).payoff
        if self.player.in_round(4).is_winner==True:
            winner4 = "Yes"
        else:
            winner4 = "No"
        
        bid5 = self.group.in_round(5).bid
        win5 = self.group.in_round(5).bot1
        price5 = self.group.in_round(5).second_highest_bid
        cost5 = self.player.in_round(5).valuation
        profit5 = self.player.in_round(5).payoff
        if self.player.in_round(5).is_winner==True:
            winner5 = "Yes"
        else:
            winner5 = "No"
        
        return dict(a=a, bid1=bid1, win1=win1, price1=price1, cost1=cost1, profit1=profit1, winner1=winner1,
        bid2=bid2, win2=win2, price2=price2, cost2=cost2, profit2=profit2, winner2=winner2,
        bid3=bid3, win3=win3, price3=price3, cost3=cost3, profit3=profit3, winner3=winner3,
        bid4=bid4, win4=win4, price4=price4, cost4=cost4, profit4=profit4, winner4=winner4,
        bid5=bid5, win5=win5, price5=price5, cost5=cost5, profit5=profit5, winner5=winner5)


page_sequence = [Intro, Auction, ResultsWaitPage, Results]
