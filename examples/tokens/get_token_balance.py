from bscscan.tokens import Tokens
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x043d9b3af52b623e54a3dF92F1682757eb29F912'
api = Tokens(contract_address='0x0cf2b5aabf844b49480dbf5e6192b873a865fae4',
             api_key=key)
balance = api.get_token_balance(address=address)
print(balance)
