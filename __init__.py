from otree.api import *

doc = """
Public good, based on Fehr & Gaechter 2000. 
"""

class C(BaseConstants):
    NAME_IN_URL = 'public_goods_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
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
