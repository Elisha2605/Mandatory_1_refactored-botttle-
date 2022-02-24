from bottle import get, request, redirect
import data


####################  Logout / GET  ######################
@get("/logout")
def _():
    user_session_jwt = request.get_cookie("jwt")
    data.SESSIONS.remove(user_session_jwt)
    
    return redirect("/login")