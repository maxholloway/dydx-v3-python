'''Example for onboarding an account and accessing private endpoints.

Usage: python -m examples.onboard
'''

from dydx3 import Client
from dydx3 import private_key_to_public_key_pair_hex
from dydx3.constants import API_HOST_ROPSTEN
from dydx3.constants import NETWORK_ID_ROPSTEN
from web3 import Web3

# Private key for your ethereum address
ETHEREUM_PRIVATE_KEY = ''

# HTTP Provider URL
WEB_PROVIDER_URL = 'https://ropsten.infura.io/v3/<INFURA_API_KEY>'

client = Client(
    network_id=NETWORK_ID_ROPSTEN,
    host=API_HOST_ROPSTEN,
    eth_private_key=ETHEREUM_PRIVATE_KEY,
    web3=Web3(Web3.HTTPProvider(WEB_PROVIDER_URL)),
)

# Set STARK key.
stark_private_key = client.onboarding.derive_stark_key()
client.stark_private_key = stark_private_key
public_x, public_y = private_key_to_public_key_pair_hex(stark_private_key)

# Onboard the account.
onboarding_response = client.onboarding.create_user(
    stark_public_key=public_x,
    stark_public_key_y_coordinate=public_y,
)
print('onboarding_response', onboarding_response)

# Query a private endpoint.
accounts_response = client.private.get_accounts()
print('accounts_response', accounts_response)
