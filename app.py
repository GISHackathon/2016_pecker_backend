from flask import Flask

from user.authentication import *

app = Flask(__name__)


if __name__ == '__main__':
    app.run()