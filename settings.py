from os import environ

SESSION_CONFIGS = [
    dict(
        name='public_goods_practice',
        display_name='Public Goods Game - Practice',
        app_sequence=['public_goods_practice'],
        num_demo_participants=1,
    ),
    dict(
        name='public_goods_punishment_practice',
        display_name='Public Goods Game with Punishment - Practice',
        app_sequence=['public_goods_punishment_practice'],
        num_demo_participants=1,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

# for security, best to set this in an environment variable in production;
# the fallback below is only meant for local/demo use.
SECRET_KEY = environ.get(
    'OTREE_SECRET_KEY',
    'gVEpKi3zA6ghSP5(yw9p5UUX6*4Z!TqTe(klQ0576F6%6kaP&R',
)
