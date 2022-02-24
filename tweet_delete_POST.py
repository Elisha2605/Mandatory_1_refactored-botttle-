from bottle import post, request, redirect
import data


#####################  admin / DELETE  ######################
@post("/tweet_delete")
def _():
    tweet_id = request.forms.get("tweet_id")
    for index, tweet in enumerate(data.TWEETS):
        if tweet["id"] == tweet_id:
            data.TWEETS.pop(index)
            return redirect("/admin")
    return redirect("/admin")