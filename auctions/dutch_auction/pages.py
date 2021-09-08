from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .datacontainer import result


class Intro(Page):
    def before_next_page(self):
        pass
        self.player.cost = self.player.random_valuation()
        self.player.bot_stop = self.player.random_valuation()


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(self):
        result_list = []
        a = self.round_number
        winning_price_current_round = self.player.in_round(a).winning_price
        is_winner_current_round: bool = self.player.in_round(a).bot_stop != self.player.in_round(a).winning_price
        profit_current_round = winning_price_current_round - self.player.in_round(
            a).cost if is_winner_current_round else '$0.00'
        total_payoff = 0
        for i in range(a):
            winning_price = self.player.in_round(i + 1).winning_price
            is_winner = self.player.in_round(i + 1).bot_stop != self.player.in_round(i + 1).winning_price
            cost = self.player.in_round(i + 1).cost
            profit = winning_price - cost if is_winner == True else '$0.00'
            winner = 'Yes' if is_winner else 'No'
            result_object = result(i + 1, cost, winning_price, is_winner, profit,winner)
            result_list.append(result_object)
        return dict(a=a, total_payoff=total_payoff, winning_price=winning_price_current_round,
                    winner=is_winner_current_round, results=result_list, profit_current_round=profit_current_round)


class Auction(Page):
    form_model = 'player'
    form_fields = ['winning_price']


page_sequence = [Intro, Auction, Results]
