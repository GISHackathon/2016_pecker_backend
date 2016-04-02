from flask import Flask

app = Flask(__name__)

from user.authentication import *
from errors.error_importer import *
from errors.errors import *


if __name__ == '__main__':
    app.run(port=80, debug=True)

