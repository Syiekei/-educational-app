# services/users/project/__init__.py

import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

# set config
# app_settings = os.getenv('APP_SETTINGS')
app_settings = 'project.config.DevelopmentConfig'
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)
# set up extensions
#db.init_app(app)

from project.my_api.users import users_blueprint
app.register_blueprint(users_blueprint)
