from flask import Flask
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "ashen_dev"
app.jinja_env.undefined = StrictUndefined

from app import views