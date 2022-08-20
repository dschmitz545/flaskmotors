from flaskmotors.api.database.database import db


class PessoaModel(db.Model):
    __tablename__ = "pessoa"

    codigo_pes = db.Column(db.Integer, primary_key=True,
                           index=True, autoincrement=True)
    cgccpf_pes = db.Column(db.String(20), unique=True, nullable=False)
    nomraz_pes = db.Column(db.String(120), unique=True, nullable=False)
    cidade_pes = db.Column(db.String(80))
    uf_pes = db.Column(db.String(2))
    cep_pes = db.Column(db.String(9))
    logra_pes = db.Column(db.String(120))
    numend_pes = db.Column(db.String(20))
    telres_pes = db.Column(db.Integer)
    dddres_pes = db.Column(db.Integer)
    telcom_pes = db.Column(db.Integer)
    dddcom_pes = db.Column(db.Integer)
    telcel_pes = db.Column(db.Integer)
    dddcel_pes = db.Column(db.Integer)

    def __init__(
        self,
        codigo_pes,
        cgccpf_pes,
        nomraz_pes,
        cidade_pes,
        uf_pes,
        cep_pes,
        logra_pes,
        numend_pes,
        telres_pes,
        dddres_pes,
        telcom_pes,
        dddcom_pes,
        telcel_pes,
        dddcel_pes,
    ):
        self.codigo_pes = codigo_pes
        self.cgccpf_pes = cgccpf_pes
        self.nomraz_pes = nomraz_pes
        self.cidade_pes = cidade_pes
        self.uf_pes = uf_pes
        self.cep_pes = cep_pes
        self.logra_pes = logra_pes
        self.numend_pes = numend_pes
        self.telres_pes = telres_pes
        self.dddres_pes = dddres_pes
        self.telcom_pes = telcom_pes
        self.dddcom_pes = dddcom_pes
        self.telcel_pes = telcel_pes
        self.dddcel_pes = dddcel_pes

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _codigo_pes):
        return cls.query.filter_by(codigo_pes=_codigo_pes).first()

    @classmethod
    def find_by_cgccpf(cls, _cgccpf_pes):
        return cls.query.filter_by(cgccpf_pes=_cgccpf_pes).first()
