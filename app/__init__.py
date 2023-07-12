from flask import Flask
from config import Config

# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'


from app import routes

# Enable debug mode
app.debug = True