import twitter


class TwitterFetcher(object):
    def fetch_data(self):
        api = twitter.Api(consumer_key='c22srMiDzXO2VxPV2x3SfEJZo',
                          consumer_secret='FVhrRBUeT2mXiOHytRqDniyx2BvKmt1CdeB2FqS6YBdFolvwQg',
                          access_token_key='924257458796851200-Wbh3lUfseYSoh7G6Sv5L9iqKQCdN3gD',
                          access_token_secret='QjM94R8ktED5diDpNqnrsol7cwO8JT9S1is0rwuw1NMnw')

        print(api.VerifyCredentials())


TwitterFetcher().fetch_data()