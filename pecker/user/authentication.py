from pecker.app import app
import requests

@app.route('/login')
def login():

    r = requests.post('https://api.twitter.com/oauth/request_token', auth='''OAuth oauth_callback="http%3A%2F%2Flocalhost%2Fsign-in-with-twitter%2F",
              oauth_consumer_key="QH9G5kSSPpFCsZ0Brs9p3Ntvw",
              oauth_nonce="ea9ec8429b68d6b77cd5600adbbb0456",
              oauth_signature="F1Li3tvehgcraF8DMJ7OyxO4w9Y%3D",
              oauth_signature_method="HMAC-SHA1",
              oauth_timestamp="1318467427",
              oauth_version="1.0"''')

    return r.text