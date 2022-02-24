import time


######################## REGEX ###############################
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

######################## COOKIES ###############################
SESSIONS = []
COOKIE_SECRET = "This is my secret"

######################## DICTS ###############################
USERS = [
    {
        "id": "a5ea9d0c-1295-4a1e-8184-e22e50ec1914", 
        "firstname": "Aicha", 
        "lastname": "Haidara", 
        "email": "a@a.com", 
        "password": "123",
    },
    {
        "id": "b6d1f3b1-c6e8-46f0-892f-19fd065cbfa6", 
        "firstname": "Elisha", 
        "lastname": "Ngoma", 
        "email": "elisha_ngoma@yahoo.fr", 
        "password": "123"
    }
]
TWEETS = [
    {
        "id": "c10118bf-60dd-4099-bca4-8c73e0489234", 
        "title": "Aïcha", 
        "description": "Haïdara",
        "time": str(time.time()) 
    },
    {
        "id": "56f41f60-7614-4e35-85a8-73dbff779e4a", 
        "title": "Elisha", 
        "description": "Haïdara",
        "time": str(time.time()) 
    }
]