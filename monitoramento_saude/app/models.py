from .database import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(10))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    medidas = db.relationship('Medida', backref='usuario', cascade='all, delete-orphan')
    treinos = db.relationship('Treino', backref='usuario', cascade='all, delete-orphan')


class Medida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)


class Treino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    tipo = db.Column(db.String(80), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    calorias = db.Column(db.Float)
    data = db.Column(db.DateTime, default=datetime.utcnow)