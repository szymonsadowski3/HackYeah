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

        new_tweets = self.api.user_timeline(screen_name=screen_name, count=20)
        alltweets.extend(new_tweets)
        return [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    def does_user_exist(self, username):
        try:
            user = self.api.get_user(username)
            return user is not None
        except tweepy.error.TweepError:
            return False


if __name__ == '__main__':
    print(TwitterUnlimitedFetcher().does_user_exist("BoniekZibiasfasf"))

