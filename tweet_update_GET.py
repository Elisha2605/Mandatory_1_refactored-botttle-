
from bottle import get, view, request, response, redirect
import data
import jwt


####################  Admin update / GET  ######################
@get("/tweet-update")
@view("tweet_update")
def _():
    tweet_id = request.params.get("tweet_id")
    for tweet in data.TWEETS:
        if tweet["id"] == tweet_id:
            id = tweet["id"]
            title = tweet["title"]
            description = tweet["description"]

            return dict(id=id, title=title, description=description)