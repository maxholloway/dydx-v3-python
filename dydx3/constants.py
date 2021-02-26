# ------------ API URLs ------------
API_HOST_MAINNET = 'https://api.dydx.exchange'
API_HOST_ROPSTEN = 'https://api.stage.dydx.exchange'
WS_HOST_MAINNET = 'wss://api.dydx.exchange/v3/ws'
WS_HOST_ROPSTEN = 'wss://api.stage.dydx.exchange/v3/ws'

# ------------ Ethereum Network IDs ------------
NETWORK_ID_MAINNET = 1
NETWORK_ID_ROPSTEN = 3

# ------------ Signature Types ------------
SIGNATURE_TYPE_NO_PREPEND = 0
SIGNATURE_TYPE_DECIMAL = 1
SIGNATURE_TYPE_HEXADECIMAL = 2

# ------------ Market Statistic Day Types ------------
MARKET_STATISTIC_DAY_ONE = '1'
MARKET_STATISTIC_DAY_SEVEN = '7'
MARKET_STATISTIC_DAY_THIRTY = '30'

# ------------ Order Types ------------
ORDER_TYPE_LIMIT = 'LIMIT'
ORDER_TYPE_STOP = 'STOP'
ORDER_TYPE_TRAILING_STOP = 'TRAILING_STOP'
ORDER_TYPE_TAKE_PROFIT = 'TAKE_PROFIT'

# ------------ Order Side ------------
ORDER_SIDE_BUY = 'BUY'
ORDER_SIDE_SELL = 'SELL'

# ------------ Time in Force Types ------------
TIME_IN_FORCE_GTT = 'GTT'
TIME_IN_FORCE_FOK = 'FOK'
TIME_IN_FORCE_IOC = 'IOC'

# ------------ Position Status Types ------------
POSITION_STATUS_OPEN = 'OPEN'
POSITION_STATUS_CLOSED = 'CLOSED'
POSITION_STATUS_LIQUIDATED = 'LIQUIDATED'

# ------------ Order Status Types ------------
ORDER_STATUS_PENDING = 'PENDING'
ORDER_STATUS_OPEN = 'OPEN'
ORDER_STATUS_FILLED = 'FILLED'
ORDER_STATUS_CANCELED = 'CANCELED'
ORDER_STATUS_UNTRIGGERED = 'UNTRIGGERED'

# ------------ Transfer Status Types ------------
TRANSFER_STATUS_PENDING = 'PENDING'
TRANSFER_STATUS_CONFIRMED = 'CONFIRMED'
TRANSFER_STATUS_QUEUED = 'QUEUED'
TRANSFER_STATUS_CANCELED = 'CANCELED'
TRANSFER_STATUS_UNCONFIRMED = 'UNCONFIRMED'

# ------------ Account Action Types ------------
ACCOUNT_ACTION_DEPOSIT = 'DEPOSIT'
ACCOUNT_ACTION_WITHDRAWAL = 'WITHDRAWAL'

# ------------ Markets ------------
MARKET_BTC_USD = 'BTC-USD'
MARKET_ETH_USD = 'ETH-USD'
MARKET_LINK_USD = 'LINK-USD'

# ------------ Assets ------------
ASSET_USDC = 'USDC'
ASSET_BTC = 'BTC'
ASSET_ETH = 'ETH'
ASSET_LINK = 'LINK'
COLLATERAL_ASSET = ASSET_USDC

# ------------ Synthetic Assets by Market ------------
SYNTHETIC_ASSET_MAP = {
    MARKET_BTC_USD: ASSET_BTC,
    MARKET_ETH_USD: ASSET_ETH,
    MARKET_LINK_USD: ASSET_LINK,
}

# ------------ Asset IDs ------------
COLLATERAL_ASSET_ID_BY_NETWORK_ID = {
    NETWORK_ID_MAINNET: int(
        '0x02893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d',
        16,
    ),
    NETWORK_ID_ROPSTEN: int(
        '0x02c04d8b650f44092278a7cb1e1028c82025dff622db96c934b611b84cc8de5a',
        16,
    ),
}
SYNTHETIC_ASSET_ID_MAP = {
    ASSET_BTC: int('0x4254432d3130000000000000000000', 16),
    ASSET_ETH: int('0x4554482d3900000000000000000000', 16),
    ASSET_LINK: int('0x4c494e4b2d37000000000000000000', 16),
}


# ------------ Asset Resolution (Quantum Size) ------------
#
# The asset resolution is the number of quantums (Starkware units) that fit
# within one "human-readable" unit of the asset. For example, if the asset
# resolution for BTC is 1e10, then the smallest unit representable within
# Starkware is 1e-10 BTC, i.e. 1/100th of a satoshi.
#
# For the collateral asset (USDC), the chosen resolution corresponds to the
# base units of the ERC-20 token. For the other, synthetic, assets, the
# resolutions are chosen such that prices relative to USDC are close to one.
ASSET_RESOLUTION = {
    ASSET_USDC: '1e6',
    ASSET_BTC: '1e10',
    ASSET_ETH: '1e9',
    ASSET_LINK: '1e7',
}

# ------------ Ethereum Transactions ------------
DEFAULT_GAS_AMOUNT = 250000
DEFAULT_GAS_MULTIPLIER = 1.5
DEFAULT_GAS_PRICE = 4000000000
DEFAULT_GAS_PRICE_ADDITION = 3
MAX_SOLIDITY_UINT = 115792089237316195423570985008687907853269984665640564039457584007913129639935  # noqa: E501
FACT_REGISTRY_CONTRACT = {
    NETWORK_ID_MAINNET: '0xBE9a129909EbCb954bC065536D2bfAfBd170d27A',
    NETWORK_ID_ROPSTEN: '0x8Fb814935f7E63DEB304B500180e19dF5167B50e',
}
STARKWARE_PERPETUALS_CONTRACT = {
    NETWORK_ID_MAINNET: '0xD54f502e184B6B739d7D27a6410a67dc462D69c8',
    NETWORK_ID_ROPSTEN: '0x014F738EAd8Ec6C50BCD456a971F8B84Cd693BBe',
}
TOKEN_CONTRACTS = {
    ASSET_USDC: {
        NETWORK_ID_MAINNET: '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
        NETWORK_ID_ROPSTEN: '0x8707A5bf4C2842d46B31A405Ba41b858C0F876c4',
    },
}
COLLATERAL_TOKEN_DECIMALS = 6

# ------------ Off-Chain Ethereum-Signed Actions ------------
OFF_CHAIN_ONBOARDING_ACTION = 'dYdX Onboarding'
OFF_CHAIN_KEY_DERIVATION_ACTION = 'dYdX STARK Key'
