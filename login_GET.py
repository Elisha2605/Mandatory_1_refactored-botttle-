from bottle import get, view



#################  LOGIN / GET  ###################
@get("/login")
@view("login")
def _():
    return