from flask import Flask
from flask_restful import Api

from flaskmotors.ext.cli import commands
from flaskmotors.ext.config import config
from flaskmotors.ext.database.database import db
from flaskmotors.ext.migrate.migrate import migrate

# from flaskmotors.ext.api import api
from flaskmotors.ext.routes import routes


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    commands.init_app(app)
    migrate.init_app(app)
    api = Api(app, prefix="/api/v1")

    # api.init_app(app)
    # app.register_blueprint(rt_api, url_prefix="/api/v1")

    # api.load_routes(api)
    routes.load_routes(api)

    return app
