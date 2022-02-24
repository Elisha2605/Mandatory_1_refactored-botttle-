from logging import root
from bottle import run, get, view, static_file, error




########  GET  ########
import home_GET
import users_GET
import signup_GET
import admin_GET
import tweet_create_GET
import tweet_update_GET
import login_GET
########  POST  #######
import signup_POST
import tweet_delete_POST
import tweet_create_POST
import tweet_update_POST
import login_POST
import logout_POST



#######  STATIC FILES  #######
@get('/static/<filename>')
def _(filename):
    return static_file(filename, root="./static")
#######  ERROR 404  #######
@error(404)
@view("404")
def _(error):
    print(error)
    return


run(host='127.0.0.1', port=8080, reloader=True, debug=True, server="paste")