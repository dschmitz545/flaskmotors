from flask_restful import Api
from ext.resources.pessoa import PessoaResource


def init_app(app):
    api = Api(app, prefix="/api/v1")
    api.init_app(app)


def load_routes(api):
    api.add_resource(PessoaResource, "/pessoas")
    return api
