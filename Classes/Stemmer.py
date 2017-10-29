import requests


class Stemmer(object):
    def __init__(self):
        self.host = "localhost"
        self.port = 8080
        self.path = "/getstem"

    def get_stem(self, stem):
        req = requests.get("http://" + self.host + ":" + str(self.port) + self.path + "/" + stem)
        return req.text
