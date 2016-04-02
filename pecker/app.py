from flask import Flask



from pecker.user.authentication import *
from pecker.errors.error_importer import *
from pecker.errors.errors import *


app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=80, debug=True)

