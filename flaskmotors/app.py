from calendar import c
from flask import Flask
from flaskmotors.api.config import config
from flaskmotors.api.database.database import db
from flaskmotors.api.cli import commands
from flaskmotors.api.routes.routes import rt_api
from flaskmotors.api.migrate.migrate import migrate


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    commands.init_app(app)
    migrate.init_app(app)
    app.register_blueprint(rt_api, url_prefix="/api/v1")

    return app
