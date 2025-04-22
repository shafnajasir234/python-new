import logging

logging.basicConfig(filename='flask_app.log', level=logging.DEBUG)

@app.route('/')
def hello_world():
    app.logger.info('Hello, World! endpoint was accessed')
    return 'Hello, World!'
