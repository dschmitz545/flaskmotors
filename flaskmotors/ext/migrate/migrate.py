from flask_migrate import Migrate

from flaskmotors.ext import models  # noqa
from flaskmotors.ext.database.database import db

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
