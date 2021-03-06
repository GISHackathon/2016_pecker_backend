from pecker import config
import flask
from flask import request
from pecker.geotools.point import Point
from pecker.geotools.point_buffer import PointBuffer
from pecker.model.error_db_handler import ErrorDbHandler
from pecker.geotools.geojson_builder import GeojsonBuilder
from pecker.app import app


@app.route('/errors/all')
def get_all_errors():
    errors = ErrorDbHandler.get_all_errors()
    gj_errors = GeojsonBuilder.build_geojson(errors)
    return flask.jsonify(**gj_errors)


@app.route('/errors/get-by-location', methods=['GET', 'POST'])
def get_errors_by_location():
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

    errors = ErrorDbHandler.get_all_errors()
    center_buffer = PointBuffer(center, config.LOC_BUFFER_RADIUS)
    for i, error in enumerate(errors):
        p = Point(error['x_coord'], error['y_coord'])
        if not center_buffer.is_point_within(p):
            errors.pop(i)
    gj_errors = GeojsonBuilder.build_geojson(errors)
    return flask.jsonify(**gj_errors)




