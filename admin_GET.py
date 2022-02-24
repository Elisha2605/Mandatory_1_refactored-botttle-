from bottle import get, view, request, redirect
import data
import jwt


####################  Admin / GET  ######################
@get("/admin")
@view("admin")
def _():
    user_session_jwt = request.get_cookie("jwt")

    if user_session_jwt not in data.SESSIONS:
        return redirect("/login")

    for session in data.SESSIONS:
        if session == user_session_jwt:
            user = jwt.decode(session, "secret", algorithms=["HS256"])
            
    return dict(tweets=data.TWEETS)