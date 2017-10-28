import tweepy


class TwitterUnlimitedFetcher(object):
    def __init__(self):
        self.consumer_key = 'c22srMiDzXO2VxPV2x3SfEJZo'
        self.consumer_secret = 'FVhrRBUeT2mXiOHytRqDniyx2BvKmt1CdeB2FqS6YBdFolvwQg'
        self.access_key = '924257458796851200-Wbh3lUfseYSoh7G6Sv5L9iqKQCdN3gD'
        self.access_secret = 'QjM94R8ktED5diDpNqnrsol7cwO8JT9S1is0rwuw1NMnw'

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        self.api = tweepy.API(auth)

    def get_all_tweets(self, screen_name):
        alltweets = []

        new_tweets = self.api.user_timeline(screen_name=screen_name, count=200)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

        while len(new_tweets) > 0:
            print("getting tweets before %s" % oldest)
            new_tweets = self.api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
            print("...%s tweets downloaded so far" % (len(alltweets)))

        outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

        return outtweets


if __name__ == '__main__':
    TwitterUnlimitedFetcher().get_all_tweets("BoniekZibi")
