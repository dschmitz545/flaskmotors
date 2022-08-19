import click
from flaskmotors.api.database.database import db
from flaskmotors.api.models import pessoa # noqa


def init_app(app):
    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        try:
            db.create_all()
        except TypeError:
            # Todo: Usar tabulate
            click.echo("Aconteceu um erro")
        else:
            click.echo("Database created!")
