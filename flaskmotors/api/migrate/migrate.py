from flask_migrate import Migrate
from flaskmotors.api.database.database import db
from flaskmotors.api import models  # noqa

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
