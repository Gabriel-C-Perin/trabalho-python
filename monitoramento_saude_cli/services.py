from storage import load_data, save_data
from models import Usuario, Medida, Treino
from utils import calcular_imc, estimar_calorias, classificar_imc


def listar_usuarios():
data = load_data()
return data['usuarios']


def criar_usuario(nome):
data = load_data()
u = Usuario.new(nome)
data['usuarios'].append(u.__dict__)
save_data(data)
return u.__dict__


def get_usuario(usuario_id):
data = load_data()
for u in data['usuarios']:
if u['id'] == usuario_id:
return u
return None


def registrar_medida(usuario_id, peso, altura):
data = load_data()
if not get_usuario(usuario_id):
raise ValueError('Usuario nao encontrado')
m = Medida.new(usuario_id, peso, altura)
data['medidas'].append(m.__dict__)
save_data(data)
return m.__dict__


def registrar_treino(usuario_id, tipo, duracao):
data = load_data()
if not get_usuario(usuario_id):
raise ValueError('Usuario nao encontrado')
calorias = estimar_calorias(tipo, duracao)
t = Treino.new(usuario_id, tipo, duracao, calorias)
data['treinos'].append(t.__dict__)
save_data(data)
return t.__dict__


def ultima_medida(usuario_id):
data = load_data()
medidas = [m for m in data['medidas'] if m['usuario_id']==usuario_id]
if not medidas:
return None
medidas.sort(key=lambda m: m['data'], reverse=True)
return medidas[0]


def relatorio_imc(usuario_id):
m = ultima_medida(usuario_id)
if not m:
raise ValueError('Nenhuma medida encontrada')
imc_val = calcular_imc(m['peso'], m['altura'])
return {'imc': imc_val, 'classificacao': classificar_imc(imc_val), 'medida': m}


def calorias_total_periodo(usuario_id):
data = load_data()
treinos = [t for t in data['treinos'] if t['usuario_id']==usuario_id]
return round(sum(t['calorias'] for t in treinos),2)