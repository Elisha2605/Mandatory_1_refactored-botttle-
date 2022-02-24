from bottle import post, request, redirect
import time
import data



#####################  admin / UPDATE  ######################
@post("/tweet-update")
def _():
    id = request.forms.get("id")
    new_title = request.forms.get("title")
    new_description = request.forms.get("description")
    for index, tweet in enumerate(data.TWEETS):

        if tweet['id'] == id:
            data.TWEETS[index]["title"] = new_title
            data.TWEETS[index]["description"] = new_description
            data.TWEETS[index]["time"] = int(time.time())
    
    return redirect("/admin")