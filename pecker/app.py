from flask import Flask

import sys

sys.path.append('..')

app = Flask(__name__)

from pecker.user.authentication import *
from pecker.errors.error_importer import *
from pecker.errors.errors import *


if __name__ == '__main__':
    app.run(port=80, debug=True)

