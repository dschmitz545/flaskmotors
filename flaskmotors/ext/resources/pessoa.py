from flaskmotors.ext.models.pessoa import PessoaModel
from flaskmotors.ext.schemas.pessoa import pessoa_schema
from flask_restful import Resource, reqparse, marshal


class PessoaResource(Resource):

    def get(self):
        pessoa = PessoaModel.query.all()
        resu = marshal(pessoa, pessoa_schema, 'pessoa')
        return resu

    def post(self):
        # person = PessoaResource.parser.parse_args()
        parser = reqparse.RequestParser()
        parser.add_argument("nomraz_pes", type=str, required=True,
                            help="O campo nomraz_pes é obrigatório")
        parser.add_argument("cgccpf_pes", type=str, required=True,
                            help="O campo cgccpf_pes é obrigatório")

        parser.add_argument("cidade_pes", type=str, required=False)
        parser.add_argument("uf_pes", type=str, required=False)
        parser.add_argument("cep_pes", type=str, required=False)
        parser.add_argument("logra_pes", type=str, required=False)
        parser.add_argument("numend_pes", type=str, required=False)
        parser.add_argument("telres_pes", type=int, required=False)
        parser.add_argument("dddres_pes", type=int, required=False)
        parser.add_argument("telcom_pes", type=int, required=False)
        parser.add_argument("dddcom_pes", type=int, required=False)
        parser.add_argument("telcel_pes", type=int, required=False)
        parser.add_argument("dddcel_pes", type=int, required=False)

        # if PessoaModel.find_by_cgccpf(parser["cgccpf_pes"]):
        # return {"message": "Pessoa informada já está cadastrada"}, 400

        pessoa = PessoaModel(**parser)
        pessoa.save_to_db()

        return {"message": "Pessoa cadastrada com sucesso"}, 201
