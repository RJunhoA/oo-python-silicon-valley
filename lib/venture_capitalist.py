from lib.funding_round import *
from lib.startup import *

class VentureCapitalist:
    all = []
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @classmethod
    def tres_commas_club(cls):
        return [v for v in cls.all if v.total_worth > 1000000]