from bottle import get, request, redirect, view
import data


####################  Admin update / GET  ######################
@get("/tweet-create")
@view("tweet_create")
def _():

    user_sessin_jwt = request.get_cookie("jwt")
    
    if user_sessin_jwt not in data.SESSIONS:
        return redirect("/login")

    return