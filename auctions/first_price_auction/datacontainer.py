"""
class to represent the results of an auction
"""
class result():
    num = 0
    bid = 0
    win = 0
    price = 0
    cost = 0
    profit = 0
    winner = 0
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
    def __init__(self, num, bid, win, price, cost, profit, winner,others_bid):
        self.num = num
        self.bid = bid
        self.win = win
        self.price = price
        self.cost = cost
        self.profit = profit
        self.winner = winner
        self.others_bid = others_bid
