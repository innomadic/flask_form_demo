from flask import Flask

app = Flask(__name__)

# this secret key should be set in a configuration file for production use
app.config['SECRET_KEY'] = 'secret321'
from app import routes