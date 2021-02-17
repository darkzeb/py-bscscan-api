from .client import Client


class Stats(Client):
    def __init__(self, api_key='YourApiKeyToken'):
        Client.__init__(self, address='', api_key=api_key)
        self.url_dict[self.MODULE] = 'stats'

    def get_total_bnb_supply(self):
        self.url_dict[self.ACTION] = 'bnbsupply'
        self.build_url()
        req = self.connect()
        return req['result']

    def get_validators(self):
        self.url_dict[self.ACTION] = 'validators'
        self.build_url()
        req = self.connect()
        return req['result']

    # NOT YET AVAILABLE IN BSCSCAN APIS
    # def get_bnb_last_price(self):
    #     self.url_dict[self.ACTION] = 'bnbprice'
    #     self.build_url()
    #     req = self.connect()
    #     return req['result']
