from flask_restful import Api
from flaskmotors.ext.resources.pessoa import PessoaResource


def load_routes(api: Api) -> Api:
    api.add_resource(PessoaResource, "/pessoas")

    return api
