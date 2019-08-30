from project import app

@app.route('/')
@app.route('/hello')
def hello():
    return 'Hello everyone'