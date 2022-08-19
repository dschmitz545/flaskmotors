from flask_restful import Resource, reqparse
from api.models.pessoa import PessoaModel


class PessoaRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("nomraz_pes", type=str, Required=True,
                        help="O campo nomraz_pes é obrigatório")
    parser.add_argument("cgccpf_pes", type=str, Required=True,
                        help="O campo cgccpf_pes é obrigatório")

    parser.add_argument("cidade_pes", type=str, Required=False)
    parser.add_argument("uf_pes", type=str, Required=False)
    parser.add_argument("cep_pes", type=str, Required=False)
    parser.add_argument("logra_pes", type=str, Required=False)
    parser.add_argument("numend_pes", type=str, Required=False)
    parser.add_argument("telres_pes", type=int, Required=False)
    parser.add_argument("dddres_pes", type=int, Required=False)
    parser.add_argument("telcom_pes", type=int, Required=False)
    parser.add_argument("dddcom_pes", type=int, Required=False)
    parser.add_argument("telcel_pes", type=int, Required=False)
    parser.add_argument("dddcel_pes", type=int, Required=False)

    def post(self):
        person = PessoaRegister.parser.parse_args()

        if PessoaModel.find_by_cgccpf(person["cgccpf_pes"]):
            return {"message": "Pessoa informada já está cadastrada"}, 400

        pessoa = PessoaModel(**person)
        pessoa.save_to_db()

        return {"message": "Pessoa cadastrada com sucesso"}, 201
