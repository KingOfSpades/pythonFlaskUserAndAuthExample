from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# instantiate application and database
app = Flask(__name__, static_folder='staticFiles')
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create login manager
login_manager = LoginManager()
login_manager.init_app(app)

import routes, models

# This will create an ad hoc cert
if __name__ == "__main__":
  app.run(ssl_context='adhoc')
