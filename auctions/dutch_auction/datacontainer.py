"""
class to represent the results of an auction
"""
class result():
    num = 0
    cost = 0
    winning_price = 0
    is_winner = False
    profit = 0
    winner =''
    """
    constructor for class
    :param num: round number
    :param bid: bid in this round for player
    :param win: win in this round for player
    :param price: price in this round for player
    :param cost: cost in this round for player
    :param profit: profit in this round for player
    :param winner: bool if player win or loose
    """
    def __init__(self, num, cost, winning_price,is_winner,profit,winner):
        self.num = num
        self.cost = cost
        self.winning_price = winning_price
        self.is_winner = is_winner
        self.profit = profit
        self.winner = winner
