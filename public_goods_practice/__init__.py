from otree.api import *

doc = """
Public good, based on Fehr & Gaechter 2000.
Practice round only: player decisions are not recorded.
"""


class C(BaseConstants):
    NAME_IN_URL = 'public_goods_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Plain numbers (not Currency) so they can be interpolated directly into
    # the page's JavaScript for the payoff calculation.
    ENDOWMENT = 20
    EFFICIENCY_FACTOR = 0.4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Practice(Page):
    timeout_seconds = 300


page_sequence = [Practice]
