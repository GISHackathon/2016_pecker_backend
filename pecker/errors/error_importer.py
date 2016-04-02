# -*- coding: utf-8 -*-

from datetime import datetime

from pecker import config
from TwitterAPI import TwitterAPI
from model.error_db_handler import ErrorDbHandler

from pecker.app import app


@app.route('/errors/import')
def import_errors():
    api = TwitterAPI(
        config.TW_CUSTOMER_KEY,
        config.TW_CUSTOMER_SECRET,
        config.TW_ACCESS_TOKEN_KEY,
        config.TW_ACCESS_TOKEN_SECRET
    )
    tweet_set = api.request('statuses/home_timeline', {'count': config.IMP_TWEET_COUNT})

    if tweet_set.status_code != 200:
        return 'Twitter request error...'

    for t in tweet_set:
        #return flask.jsonify(**t)
        process_tweet(t)

    return '<br/>'.join(['%s:: %s' % (key, value) for (key, value) in t.items()])


def process_tweet(tweet):
    x_coord, y_coord = get_coordinates(tweet)
    if not (x_coord and y_coord):
        return
    tweet_type = get_tweet_type(tweet)

    ErrorDbHandler.import_tweet(
        tweet['id_str'],
        tweet['user']['id'],
        tweet['text'],
        x_coord,
        y_coord,
        formate_tweet_date(tweet['created_at']),
        tweet_type,
        get_img_url(tweet)
    )


def get_coordinates(tweet):
    if tweet['coordinates']:
        x_coord = tweet['coordinates']['coordinates'][1]
        y_coord = tweet['coordinates']['coordinates'][0]
    elif tweet['geo']:
        x_coord = tweet['geo']['coordinates'][1]
        y_coord = tweet['geo']['coordinates'][0]
    elif tweet['place']:
        coords = tweet['place']['bounding_box']['coordinates']
        x_max = coords[-1][1]
        y_min = coords[-1][0]
        x_min = coords[1][1]
        y_max = coords[1][0]
        x_coord = (x_min + x_max) / 2
        y_coord = (y_min + y_max) / 2
    else:
        return None, None
    return x_coord, y_coord


def get_tweet_type(tweet):
    for tag in tweet['entities']['hashtags']:
        if tag['text'].lower() in config.ERR_TYPES:
            return tag['text'].lower()
    return None


def formate_tweet_date(date):
    parts = date.split(' ')
    filtered_parts = parts[0:-2] + parts[-1:]
    date_str = ' '.join(filtered_parts)
    tweet_date = datetime.strptime(
        date_str,
        '%a %b %d %H:%M:%S %Y'
    )
    return str(tweet_date)


def get_img_url(tweet):
    if tweet['entities']:
        if tweet['entities']['media']:
            return tweet['entities']['media'][0]['media_url']
    return None
