def init_app(app):
    app.config["SECRET_KEY"] = "1234"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://master:laranjauva@172.30.0.2:5432/flaskmotors"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SWAGGER"] = {"title": "FlaskMotors API"}
    app.config["DEBUG"] = True


# "postgresql://master:laranjauva@172.30.0.2:5432/flaskmotors"
# "sqlite:///flaskmotors.db"
