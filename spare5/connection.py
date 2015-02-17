CREDENTIALS = {}


def register(username, token):
    global CREDENTIALS
    CREDENTIALS = {
        'username': username,
        'token': token
    }
