from os import environ

SESSION_CONFIGS = [
    # dict(
    #    name='public_goods',
    #    display_name="Public Goods",
    #    num_demo_participants=3,
    #    app_sequence=['public_goods', 'payment_info']
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)
SESSION_CONFIGS=[
    dict(
        name = 'First_Price_Auction',
        display_name='First Price Auction',
        num_demo_participants=1,
        app_sequence=['first_price_auction']
    ),
    dict(
        name = 'Second_Price_Auction',
        display_name='Second Price Auction',
        num_demo_participants=1,
        app_sequence=['second_price_auction']
    ),
    dict(
        name = 'Dutch_Auction',
        display_name='Dutch Auction',
        num_demo_participants=1,
        app_sequence=['dutch_auction']
    ),
    dict(
        name = 'English_Auction',
        display_name='English Auction',
        num_demo_participants=1,
        app_sequence=['english_auction']
    )
]
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False
ROOMS = [
    dict(
        name='First_Price_Auction',
        display_name='First Price Auction'
    ),
    dict(
        name='Second_Price_Auction',
        display_name='Second Price Auction'
    ),
    dict(
        name='Dutch_Auction',
        display_name='Dutch Auction'
    ),
    dict(
        name='English_Auction',
        display_name='English Auction'
    )
]
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'k87&f*4@pj*%kgfeiskq+4(i$-a((1pu3l5dsqamu+=s-v^_gq'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
