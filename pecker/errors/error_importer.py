
import urllib2

from pecker.model.error_db_handler import ErrorDbHandler
from pecker.app import app
from pecker import config
import json


@app.route('/errors/import')
def import_errors():
    try:
        resp = urllib2.urlopen(config.RU_WFS_URL)
    except urllib2.URLError as e:
        print 'err geoserver request...'
        return
    data_json = json.load(resp)
    for f in data_json['features'][:config.IMP_ERR_COUNT]:
        coord = f['geometry']['coordinates']
        kat_id = f['properties']['kod']
        ErrorDbHandler.import_error(kat_id, coord[0], coord[1])
    return


