from flask import Flask
from app.extensions import db, migrate
from app.main.routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_blueprint)

    return app
