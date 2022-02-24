
from bottle import post, request, redirect, response
import uuid
import data
import re
import jwt



####################  Login / POST  ######################
@post("/login")
def _():

    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    
    if not user_email:
        return redirect("/login?error=user_email")
    if not re.match(data.REGEX_EMAIL, user_email):
        return redirect("/login?error=user_email")

    if not user_password:
        return redirect(f"/login?error=user_passowrd&user_email={user_email}")
    if not 3 <= len(user_password) <= 30:
        return redirect(f"/login?error=user_password&user_email={user_email}")

    for user in data.USERS:
        if user["email"] == user_email:
            if  user["password"] == user_password:
                
                session_id = str(uuid.uuid4())

                encode_jwt = jwt.encode({"first_name": user["firstname"], "last_name": user["lastname"], "session_id": session_id}, "secret", algorithm="HS256")
                data.SESSIONS.append(encode_jwt)
                
                response.set_cookie("jwt", encode_jwt)
                
                return redirect("/admin")
            else: 
                return redirect(f"/login?error=user_password&user_email={user_email}")
    
    return redirect("/login?error=no-user-found")