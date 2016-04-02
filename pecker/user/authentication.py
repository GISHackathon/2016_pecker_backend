from pecker.app import app
import requests
import oauth2 as oauth
import urlparse
from flask import redirect
import uuid
from pecker.model.session_db_handler import SessionDbHandler
import Cookie

@app.route('/login')
def login():
    # init cookies
    C = Cookie.SimpleCookie()

    # Create your consumer with the proper key/secret.
    consumer = oauth.Consumer(key="QH9G5kSSPpFCsZ0Brs9p3Ntvw", 
        secret="qDcFA4afHRo3VJvvANQ3BTITHg2GdQYTGzATpth5caYmmTk9dO")

    # Request token URL for Twitter.
    request_token_url = "https://api.twitter.com/oauth/request_token"

    # Create our client.
    client = oauth.Client(consumer)

    # The OAuth Client request works just like httplib2 for the most part.
    resp, content = client.request(request_token_url, "GET")
    
    results = urlparse.parse_qsl(content)

    if results[1][0]=='oauth_verifier':
        uid = C["session_id"]
        C = Cookie.SimpleCookie()
        puvodni = SessionDbHandler.get_session(uid, "oauth_token")
        if results[0][1]==puvodni:
            return "ok"
        else: 
            return "Cannot log in."
    else:
        uid = str(uuid.uuid4())
        C["session_id"] = uid
        SessionDbHandler.create_session(uid, "oauth_token", results[0][1])
        return redirect('https://api.twitter.com/oauth/authenticate?oauth_token=' + str(results[0][1]))

   