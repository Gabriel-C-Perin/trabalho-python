from math import floor

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return floor(imc * 1000) / 1000  # 3 casas decimais sem arredondar

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def estimar_calorias(tipo, duracao, peso=70):
    tipo = tipo.lower()
    if "corr" in tipo:
        met = 7
    elif "camin" in tipo:
        met = 3
    elif "muscul" in tipo:
        met = 4
    else:
        met = 5

    horas = duracao / 60
    return floor(met * peso * horas * 1000) / 1000