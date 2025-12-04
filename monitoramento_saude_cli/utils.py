def calcular_imc(peso, altura):
if altura <= 0:
raise ValueError("Altura deve ser maior que zero")
return round(peso / altura ** 2, 2)


def classificar_imc(imc):
if imc < 18.5:
return 'Abaixo do peso'
elif imc < 25:
return 'Normal'
elif imc < 30:
return 'Sobrepeso'
return 'Obesidade'


def estimar_calorias(tipo, duracao_min):
tipo = tipo.lower()
met_map = {'caminhada':3.5,'corrida':9.8,'bicicleta':7.5,'hiit':10,'musculacao':6.0}
met = met_map.get(tipo, 5.0)
peso_medio = 70.0
return round(met * 3.5 * peso_medio / 200 * duracao_min, 2)