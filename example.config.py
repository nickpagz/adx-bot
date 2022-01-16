TC_ACCOUNT_ID = ''
TC_API_KEY = ''
TC_API_SECRET = ''
BASE_URL = 'https://api.3commas.io'

API_KEY = ''
SECRET_KEY = ''
SUB_ACCOUNT = ''
PAIRS_BLACKLIST = ['DMG-PERP', 'BRZ-PERP', 'PERP/USD', 'SRN-PERP', 'PRIV-PERP', 'SHIB-PERP']
MAX_OPEN_POSITIONS = 10
FUNDS_USAGE = 0.9
TF = 15 # Timeframe - always in minutes - Greater than 1 minute, less than 1 day.
ADX_LENGTH = 14
EMA_LENGTH = 20
EMA_SMOOTHING = 3
DEAL_BOT_RATIO_WARNING = 0.75
CLOSE_DEALS_WITH_BOT = True  # WARNING: Will close all open positions with no equivalent enabled bots.
EARLY_CLOSE = True
CLOSE_DEALS = False # Allow bot to close deals on opposite signals. Use False to manually rescue red bags.

# 3Commas Bot Settings
BASE_ORDER_VOLUME = 10 #IN USD
TAKE_PROFIT = 1.5
SAFETY_ORDER_VOLUME = 10
MARTINGALE_VOLUME_COEFFICIENT = 1.2
MARTINGALE_STEP_COEFFICIENT = 1.55
MAX_SAFETY_ORERS = 6
ACTIVE_SAFETY_ORDERS_COUNT = 5
SAFETY_ORDER_STEP_PERCENTAGE = 0.21
LEVERAGE_CUSTOM_VALUE = 3

# Used When Updating Bot Settings
STOP_LOSS_TYPE = 'stop_loss_and_disable_bot'  # or stop_loss
STOP_LOSS_PERCENTAGE = 0
STOP_LOSS_TIMEOUT_ENABLED = False
STOP_LOSS_TIMEOUT_IN_SECONDS = 300
START_ORDER_TYPE = 'market'
