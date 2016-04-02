
from pecker.app import app
from pecker.model.error_db_handler import  ErrorDbHandler
import flask


@app.route('/errors/get-all')
def get_all_errors():
    res = {'errors': ErrorDbHandler.get_all_errors()}
    return flask.jsonify(**res)



