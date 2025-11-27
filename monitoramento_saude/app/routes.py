from flask import Blueprint, request, jsonify
from .models import Usuario, Medida, Treino
from .utils import calcular_imc, estimar_calorias, classificar_imc
from .database import db

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def home():
    return "<h1>Bem-vindo ao App de Monitoramento de Saúde</h1>"


@bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    u = Usuario(nome=data['nome'], idade=data.get('idade'), sexo=data.get('sexo'))
    db.session.add(u)
    db.session.commit()
    return jsonify({'id': u.id, 'nome': u.nome}), 201


@bp.route('/usuarios/<id>/medidas', methods=['POST'])
def registrar_medida(id):
    data = request.json
    m = Medida(usuario_id=id, peso=data['peso'], altura=data['altura'])
    db.session.add(m)
    db.session.commit()
    return jsonify({'msg': 'Medida registrada'}), 201


@bp.route('/usuarios/<id>/treinos', methods=['POST'])
def registrar_treino(id):
    data = request.json
    calorias = estimar_calorias(data['tipo'], data['duracao'])
    t = Treino(usuario_id=id, tipo=data['tipo'], duracao=data['duracao'], calorias=calorias)
    db.session.add(t)
    db.session.commit()
    return jsonify({'calorias': calorias}), 201


@bp.route('/usuarios/<id>/imc', methods=['GET'])
def imc(id):
    m = Medida.query.filter_by(usuario_id=id).order_by(Medida.data.desc()).first()
    if not m:
        return jsonify({'erro': 'Nenhuma medida encontrada'}), 404

    imc_val = calcular_imc(m.peso, m.altura)
    return jsonify({'imc': imc_val, 'classificacao': classificar_imc(imc_val)})
