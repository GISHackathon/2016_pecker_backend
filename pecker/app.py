from flask import Flask

import sys

sys.path.append('..')

app = Flask(__name__)

from pecker.user.authentication import *
from pecker.corrections.correction_importer import *
from pecker.corrections.corrections import *
from pecker.errors.error_importer import *
from pecker.errors.errors import *
from flask import Flask, session
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.url': '127.0.0.1:11211',
    'session.data_dir': './cache',
}


class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        session.save()

if __name__ == '__main__':
    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.session_interface = BeakerSessionInterface()

    app.run(port=80, debug=True)



