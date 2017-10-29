from flask import Flask, render_template, jsonify, json

from Classes.TweetToCategoryMatcher import TweetToCategoryMatcher

app = Flask(__name__)
categories_matcher = TweetToCategoryMatcher()


@app.route('/')
def index():
    return render_template('react.html')


@app.route('/user/<user>/links')
def get_links(user):
    return json.dumps({
        "links": categories_matcher.get_links_for_user(user)
    })


@app.route('/user/<user>/exists')
def does_user_exist(user):
    return json.dumps({
        "exists": categories_matcher.tweets_fetcher.does_user_exist(user)
    })

if __name__ == '__main__':
    app.run(debug=True)
