from pecker.app import app
import requests
import oauth2 as oauth
import urlparse

@app.route('/login')
def login():

    # Create your consumer with the proper key/secret.
    consumer = oauth.Consumer(key="QH9G5kSSPpFCsZ0Brs9p3Ntvw", 
        secret="qDcFA4afHRo3VJvvANQ3BTITHg2GdQYTGzATpth5caYmmTk9dO")

    # Request token URL for Twitter.
    request_token_url = "https://api.twitter.com/oauth/request_token"

    # Create our client.
    client = oauth.Client(consumer)

    # The OAuth Client request works just like httplib2 for the most part.
    resp, content = client.request(request_token_url, "GET")

    return str(type(content))

   