from bottle import post, request, redirect
import uuid
import time
import data



####################  TWEET CREATE / POST  ######################
@post("/tweet-create")
def _():
    
    tweet_id = str(uuid.uuid4())
    title = request.forms.get("title")
    description = request.forms.get("description")

    new_tweet = {
        "id": tweet_id,
        "title": title, 
        "description": description,
        "time": str(time.time())
    }

    data.TWEETS.append(new_tweet)

    return redirect("/admin")