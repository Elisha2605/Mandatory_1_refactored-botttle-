from bottle import post, redirect, request
import uuid
import data
import re


################# POST USERS ###################
@post("/signup")
def _():
 
    ###### VALIDATION ######

    #check if the vriable was passed in the form
    if not request.forms.get("user_first_name"):
        return redirect("/signup?error=user_first_name")

    if not request.forms.get("user_last_name"):
        return redirect("/signup?error=user_last_name")
        
    if not re.match(data.REGEX_EMAIL, request.forms.get("user_email")):
        return redirect("/signup?error=user_email")
    
    if not request.forms.get("user_password"):
        return redirect("/signup?error=user_password")

    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")

    # check the password and put back values into fields
    if len(request.forms.get("user_password")) < 3:
        return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    
    if len(request.forms.get("user_password")) > 50:
        return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")

    new_user = {
        "id": user_id, 
        "firstname": user_first_name, 
        "lastname": user_last_name, 
        "email": user_email, 
        "password": user_password
    }

    data.USERS.append(new_user)
    
    return redirect("/users")