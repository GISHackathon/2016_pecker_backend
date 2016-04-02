from pecker.app import app
from requests import requests

@app.route('/login')
def login():

    r = requests.post('https://api.twitter.com/oauth/request_token')

    return r.text