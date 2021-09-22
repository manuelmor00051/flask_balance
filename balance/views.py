from . import app

@app.route('/')
def index():
    return "Flask funcionando"