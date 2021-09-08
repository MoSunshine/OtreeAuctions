from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .datacontainer import result


class Intro(Page):
    def before_next_page(self):
        self.player.cost = self.player.random_valuation()
        self.player.bot_bid = self.player.random_valuation()
        # self.group.bot2 = self.player.random_valuation()


class Auction(Page):
    form_model = 'player'
    form_fields = ['bid']

    # def before_next_page(self):
    #     'highest'
    # self.group.highest()
    def vars_for_template(self):
        a = self.round_number
        cost = self.player.cost;
        return dict(a=a, cost=cost)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'highest'
    # 'highest'
    # def before_next_page(player):
    # "set_payoff"


class Results(Page):

    def vars_for_template(self):
        a = self.round_number
        result_list = []
        payoff = 0
        for i in range(a):
            bid = self.player.in_round(i + 1).bid
            win = win = True if self.player.in_round(i + 1).bid < self.player.in_round(i + 1).bot_bid else False
            price = self.player.in_round(i + 1).bot_bid if win else self.player.in_round(i + 1).bid
            cost = self.player.in_round(i + 1).cost
            profit = price - cost if win else '$0.00'
            others_bid = self.player.in_round(i + 1).bot_bid
            if win:
                winner = "Yes"
            else:
                winner = "No"
            result_object = result(i + 1, bid, win, price, cost, profit, winner, others_bid)
            result_list.append(result_object)
        return dict(results=result_list, a=a, bid=bid, win=win, price=price, profit=profit, winner=winner,
                    payoff=payoff, others_bid=others_bid)


page_sequence = [Intro, Auction, Results]
