from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from config import Config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager.init_app(app)
    bootstrap.init_app(app)


    return app