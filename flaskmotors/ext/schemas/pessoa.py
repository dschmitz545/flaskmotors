from flask_restful import fields

pessoa_schema = {
    "codigo_pes": fields.Integer,
    "cgccpf_pes": fields.String,
    "nomraz_pes": fields.String,
    "cidade_pes": fields.String,
    "uf_pes": fields.String,
    "cep_pes": fields.String,
    "logra_pes": fields.String,
    "numend_pes": fields.String,
    "telres_pes": fields.Integer,
    "dddres_pes": fields.Integer,
    "telcom_pes": fields.Integer,
    "dddcom_pes": fields.Integer,
    "telcel_pes": fields.Integer,
    "dddcel_pes": fields.Integer
}
