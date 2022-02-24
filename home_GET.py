from bottle import get, view


######################## Home / GET ###############################
@get('/')
@view('index')
def _():
    return