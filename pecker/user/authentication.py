from pecker.app import app
import requests
import oauth2 as oauth


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
    return resp + content

    #r = requests.post('https://api.twitter.com/oauth/request_token', auth='OAuth oauth_callback="http%3A%2F%2Flocalhost%2Fsign-in-with-twitter%2F",               oauth_consumer_key="QH9G5kSSPpFCsZ0Brs9p3Ntvw",              oauth_nonce="ea9ec8429b68d6b77cd5600adbbb0456",              oauth_signature="F1Li3tvehgcraF8DMJ7OyxO4w9Y%3D",              oauth_signature_method="HMAC-SHA1",              oauth_timestamp="1318467427",              oauth_version="1.0"')

    #return r.text