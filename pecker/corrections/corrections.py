from pecker import config
import flask
from flask import request
from pecker.geotools.point import Point
from pecker.geotools.point_buffer import PointBuffer
from pecker.model.correction_db_handler import CorrectionDbHandler
from pecker.geotools.goujeson_builder import GeojsonBuilder
from pecker.app import app


@app.route('/corrections/all')
def get_all_corrections():
    corrections = CorrectionDbHandler.get_all_errors()
    gj_corrections = GeojsonBuilder.build_geojson(corrections)
    return flask.jsonify(**gj_corrections)


@app.route('/corrections/get-by-location', methods=['GET', 'POST'])
def get_corrections_by_location():
    if request.method == 'POST':
        center = Point(
            request.form['x_coord'],
            request.form['y_coord']
        )
    else:
        center = Point(
            request.args.get('x_coord'),
            request.args.get('y_coord')
        )

    corrections = CorrectionDbHandler.get_all_errors()
    center_buffer = PointBuffer(center, config.LOC_BUFFER_RADIUS)
    for i, correction in enumerate(corrections):
        p = Point(correction['x_coord'], correction['y_coord'])
        if not center_buffer.is_point_within(p):
            corrections.pop(i)
    gj_corrections = GeojsonBuilder.build_geojson(corrections)
    return flask.jsonify(**gj_corrections)




