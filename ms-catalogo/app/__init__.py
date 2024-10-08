from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config
import os
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    app = Flask(__name__)
    #app.config.from_object('app.config.Config')
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)
    
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.route import catalogo_bp
        app.register_blueprint(catalogo_bp)

    return app
