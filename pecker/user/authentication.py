from pecker.app import app


@app.route('/login')
def login():
    return 'login'