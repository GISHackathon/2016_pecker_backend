from pecker.app import app
import urlparse
from flask import redirect
from flask import request
import oauth2 as oauth
from pecker import config
from flask import session
from TwitterAPI import TwitterAPI
from pecker.model.user_db_handler import UserDbHandler
import json

consumer_key = config.TW_CUSTOMER_KEY
consumer_secret = config.TW_CUSTOMER_SECRET

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

@app.route('/login')
def login():
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response %s." % resp['status'])

    request_token = dict(urlparse.parse_qsl(content))

    session["oauth_token"] = request_token['oauth_token']
    session["oauth_token_secret"] = request_token['oauth_token_secret']

    session.save()

    return redirect(authorize_url + "?oauth_token=" + request_token['oauth_token'])


@app.route('/login2')
def login2():

    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    token = oauth.Token(session['oauth_token'],
                        session['oauth_token_secret'])
    token.set_verifier(oauth_verifier)
    client = oauth.Client(consumer, token)

    resp, content = client.request(access_token_url, "POST")
    access_token = dict(urlparse.parse_qsl(content))

    if len(access_token)==0:
        return "Autorizacni token vyprsel, prihlaste se prosim znovu."
    else:

        # zde je jiz dostupne username, ale pro vice info o uzivateli jeste nasleduje request na account/verify_credentials
        username = access_token["screen_name"]

        token2 = oauth.Token(access_token["oauth_token"],
                             access_token["oauth_token_secret"])

        client2 = oauth.Client(consumer, token2)
        resp2, content2 = client2.request("https://api.twitter.com/1.1/account/verify_credentials.json", "GET")

        # save user details to the db
        save_user_to_db(json.loads(content2))

        return str(content2)


def save_user_to_db(user_data):
    UserDbHandler.create_user((user_data))


   