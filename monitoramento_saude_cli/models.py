from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class Usuario:
id: str
nome: str


@staticmethod
def new(nome: str):
return Usuario(id=str(uuid.uuid4()), nome=nome)


@dataclass
class Medida:
id: str
usuario_id: str
peso: float
altura: float
data: str


@staticmethod
def new(usuario_id: str, peso: float, altura: float):
return Medida(id=str(uuid.uuid4()), usuario_id=usuario_id, peso=peso, altura=altura, data=datetime.utcnow().isoformat())


@dataclass
class Treino:
id: str
usuario_id: str
tipo: str
duracao: int
calorias: float
data: str


@staticmethod
def new(usuario_id: str, tipo: str, duracao: int, calorias: float):
return Treino(id=str(uuid.uuid4()), usuario_id=usuario_id, tipo=tipo, duracao=duracao, calorias=calorias, data=datetime.utcnow().isoformat())