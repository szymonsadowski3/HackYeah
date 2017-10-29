from Classes.PythonMySql import MySqlWrapper
from Classes.Stemmer import Stemmer
from Classes.TweetClassifier import TweetClassifier
from Classes.TwitterUnlimitedFetcher import TwitterUnlimitedFetcher


class TweetToCategoryMatcher(object):
    def __init__(self):
        self.tweet_classifier = TweetClassifier()
        self.tweets_fetcher = TwitterUnlimitedFetcher()
        self.mysql_wrapper = MySqlWrapper()
        self.stemmer = Stemmer()

    def get_links_for_user(self, user):
        categories_links = []
        tweets = list(self.tweets_fetcher.get_all_tweets(user))

        for index, tweet in enumerate(tweets):
            print(index)
            categories_links.extend(self.get_category_for_tweet(tweet[2].decode('utf8')))

        links_sorted = sorted(categories_links, key=lambda x: x[1], reverse=True)
        links = [link[2] for link in links_sorted]

        return list(set(links))

    def get_list_of_word_to_ignore(self):
        return self.mysql_wrapper.fetch_rows_from_query("SELECT dic_word FROM `dictionary` order by dic_count "
                                                        "DESC LIMIT 30")

    def get_category_for_tweet(self, tweet):
        list_of_words_to_ignore = self.get_list_of_word_to_ignore()
        words = tweet.split(" ")
        substracted_list = [word for word in words if word not in list_of_words_to_ignore]
        return self._get_category_for_list_of_words(substracted_list)

    def _get_category_for_list_of_words(self, list_of_words):
        list_of_stemmed_words = [self.stemmer.get_stem(word) for word in list_of_words]

        query = ("SELECT prd_name, pdc_count/pdc_in_article, prd_link FROM products_dict, dictionary, products "
                 "WHERE dic_id = pdc_dic_id AND prd_id = pdc_prd_id AND dic_word "
                 "IN ({})".format(', '.join(["'{}'".format(word) for word in list_of_stemmed_words])))

        return self.mysql_wrapper.fetch_rows_from_query(query)


# TweetToCategoryMatcher().get_links_for_user("BoniekZibi")