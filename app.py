from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./database.db"
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    app.secret_key = "SECRET KEY"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from user import User

    @login_manager.user_loader
    def log_user(uid):
        return User.query.get(uid)

    bcrypt = Bcrypt(app)

    from routes import register_routes
    register_routes(app, db, bcrypt)

    migrate = Migrate(app,db)

    return app



