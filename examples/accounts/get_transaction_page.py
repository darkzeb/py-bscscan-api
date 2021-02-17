from bscscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x043d9b3af52b623e54a3dF92F1682757eb29F912'

api = Account(address=address, api_key=key)
transactions = api.get_transaction_page(page=1, offset=10000, sort='des')
print(transactions)
