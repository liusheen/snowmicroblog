from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! \nI'm Arxen. \nThanks"
