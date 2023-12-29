from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
# CREATING INSTANCE OF FLASK
app = Flask(__name__)

# CONFIGURING SQLALCHEMY DATABASE URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_adda.db"
app.config["SECRET_KEY"] = 'da1edc361505d22453af9fa9f72ede6a'

# CREATING INSTANCE OF DATABASE
db = SQLAlchemy(app)

# INITIALIZING MIGRATE COMMAND
migrate = Migrate(app, db)

#CREATEING INSTANCE FOR BCRYPT
bcrypt = Bcrypt(app)

#CREATED INSTANCE OF LOGINMANAGER AND LOA



from blog_app import routes
from blog_app import models


