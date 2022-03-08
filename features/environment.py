import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from src.app import app

# Set up the flask app to run before all tests
# https://medium.com/@sannidhi.s.t/bdd-for-flask-application-using-behave-selenium-fc6ec338c0e6
def before_all(context):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

def after_all(context):
    context.server.shutdown()
    context.pa_app.join()