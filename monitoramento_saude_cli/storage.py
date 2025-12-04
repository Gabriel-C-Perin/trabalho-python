import json
import os

DATA_FILE = 'dados.json'

# Inicializa estruturas
usuarios = []
medidas = []
treinos = []

# Função para carregar dados
def carregar():
    global usuarios, medidas, treinos
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                usuarios = data.get('usuarios', [])
                medidas = data.get('medidas', [])
                treinos = data.get('treinos', [])
        except json.JSONDecodeError:
            # Se arquivo estiver vazio ou inválido, inicia listas vazias
            usuarios = []
            medidas = []
            treinos = []

# Função para salvar dados
def salvar():
    with open(DATA_FILE, 'w') as f:
        json.dump({'usuarios': usuarios, 'medidas': medidas, 'treinos': treinos}, f, indent=4)

# Funções do CLI
def criar_usuario(nome):
    uid = len(usuarios) + 1
    usuario = {'id': uid, 'nome': nome}
    usuarios.append(usuario)
    salvar()
    return usuario

def listar_usuarios():
    return usuarios

def registrar_medida(usuario_id, peso, altura):
    mid = len(medidas) + 1
    medida = {'id': mid, 'usuario_id': usuario_id, 'peso': peso, 'altura': altura}
    medidas.append(medida)
    salvar()
    return medida

def registrar_treino(usuario_id, tipo, duracao):
    tid = len(treinos) + 1
    calorias = duracao * 10  # cálculo simples
    treino = {'id': tid, 'usuario_id': usuario_id, 'tipo': tipo, 'duracao': duracao, 'calorias': calorias}
    treinos.append(treino)
    salvar()
    return treino

def relatorio_imc(usuario_id):
    user_medidas = [m for m in medidas if m['usuario_id'] == usuario_id]
    if not user_medidas:
        raise Exception("Nenhuma medida encontrada")
    m = user_medidas[-1]
    imc = m['peso'] / (m['altura'] ** 2)
    classificacao = 'Normal' if 18.5 <= imc <= 24.9 else 'Acima' if imc > 24.9 else 'Abaixo'
    return {'imc': round(imc,2), 'classificacao': classificacao, 'medida': m}

def calorias_total_periodo(usuario_id):
    user_treinos = [t for t in treinos if t['usuario_id'] == usuario_id]
    return sum(t['calorias'] for t in user_treinos)

# Carregar dados ao iniciar
carregar()