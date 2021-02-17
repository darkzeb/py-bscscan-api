from bscscan.stats import Stats
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

# call with default address, The DAO
api = Stats(api_key=key)
validators = api.get_validators()
print(validators)
