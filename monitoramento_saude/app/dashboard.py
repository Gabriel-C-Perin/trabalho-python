from flask import Blueprint, render_template
from .models import Medida, Treino, Usuario
import matplotlib.pyplot as plt
import os

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

STATIC_DIR = 'static/dash'
os.makedirs(STATIC_DIR, exist_ok=True)

@bp.route('/<id>')
def dash(id):
    usuario = Usuario.query.get(id)
    medidas = Medida.query.filter_by(usuario_id=id).all()
    treinos = Treino.query.filter_by(usuario_id=id).all()

    # gráfico de peso
    peso_img = f'{STATIC_DIR}/peso_{id}.png'
    if medidas:
        plt.figure()
        plt.plot([m.data for m in medidas], [m.peso for m in medidas])
        plt.tight_layout()
        plt.savefig(peso_img)
        plt.close()

    return render_template('dashboard.html', usuario=usuario, peso_img=peso_img)