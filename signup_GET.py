from bottle import get, view, request
import data


################# SIGNUP / GET ###################
@get("/signup")
@view("signup")
def _():

    # Get query string from {signup_POST}
    error = request.params.get("error")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    user_email = request.params.get("user_email")

    return dict(
        users=data.USERS,
        error=error,
        user_first_name=user_first_name,
        user_last_name=user_last_name,
        user_email=user_email
    )