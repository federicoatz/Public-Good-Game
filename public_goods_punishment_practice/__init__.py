from otree.api import *

doc = """
Public good with costly punishment, based on Fehr & Gaechter 2000.
Practice round only: player decisions are not recorded.
"""


class C(BaseConstants):
    NAME_IN_URL = 'public_goods_punishment_practice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Plain numbers (not Currency) so they can be interpolated directly into
    # the page's JavaScript for the payoff calculation.
    ENDOWMENT = 20
    EFFICIENCY_FACTOR = 0.5
    # Fixed, deterministic contributions for the 3 simulated co-players, so
    # participants can reason about (and reproduce) the practice outcome.
    OTHER_CONTRIBUTIONS = [0, 10, 20]
    # Removing 1 unit from a target's payoff costs the punisher this many units.
    PUNISHMENT_COST_RATIO = 0.5
    MAX_PUNISHMENT_PER_TARGET = 20


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
