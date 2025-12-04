import sys
from storage import *

def escolha(msg, opts):
    print(msg)
    for i, o in enumerate(opts, 1):
        print(f"{i}. {o}")
    try:
        s = input('> ').strip()
        if s == '':
            return None
        v = int(s)
        if 1 <= v <= len(opts):
            return v
    except Exception:
        return None
    return None

def input_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print('Valor invalido')

def selecionar_usuario():
    usuarios_disp = listar_usuarios()
    if not usuarios_disp:
        print('Nenhum usuario cadastrado')
        return None
    for i, u in enumerate(usuarios_disp, 1):
        print(f"{i}. {u['nome']} (id: {u['id']})")
    try:
        s = int(input('Escolha (numero): '))
        if 1 <= s <= len(usuarios_disp):
            return usuarios_disp[s-1]['id']
    except Exception:
        print('Selecao invalida')
    return None

def cmd_criar_usuario():
    nome = input('Nome do usuario: ').strip()
    if not nome:
        print('Nome vazio')
        return
    u = criar_usuario(nome)
    print('Usuario criado:', u['id'])

def cmd_registrar_medida():
    usuario_id = selecionar_usuario()
    if not usuario_id:
        return
    peso = input_float('Peso (kg): ')
    altura = input_float('Altura (m): ')
    try:
        m = registrar_medida(usuario_id, peso, altura)
        print('Medida registrada com id', m['id'])
    except Exception as e:
        print('Erro:', e)

def cmd_registrar_treino():
    usuario_id = selecionar_usuario()
    if not usuario_id:
        return
    tipo = input('Tipo de treino: ').strip()
    try:
        duracao = int(input('Duracao (minutos): '))
        t = registrar_treino(usuario_id, tipo, duracao)
        print('Treino registrado. Calorias estimadas:', t['calorias'])
    except Exception as e:
        print('Erro:', e)

def cmd_ver_imc():
    usuario_id = selecionar_usuario()
    if not usuario_id:
        return
    try:
        r = relatorio_imc(usuario_id)
        print('IMC:', r['imc'], 'Classificacao:', r['classificacao'])
        print('Ultima medida:', r['medida'])
    except Exception as e:
        print('Erro:', e)

def cmd_relatorio_calorias():
    usuario_id = selecionar_usuario()
    if not usuario_id:
        return
    total = calorias_total_periodo(usuario_id)
    print('Calorias totais registradas:', total)

def main_loop():
    while True:
        print('\n=== Monitoramento de Saude (CLI) ===')
        opt = escolha('Escolha uma opcao:', [
            'Criar usuario',
            'Registrar medida',
            'Registrar treino',
            'Ver IMC e classificacao',
            'Relatorio: calorias totais',
            'Listar usuarios',
            'Sair'
        ])
        if opt is None:
            print('Opcao invalida')
            continue
        if opt == 1:
            cmd_criar_usuario()
        elif opt == 2:
            cmd_registrar_medida()
        elif opt == 3:
            cmd_registrar_treino()
        elif opt == 4:
            cmd_ver_imc()
        elif opt == 5:
            cmd_relatorio_calorias()
        elif opt == 6:
            usuarios_disp = listar_usuarios()
            if not usuarios_disp:
                print('Nenhum usuario')
            else:
                for u in usuarios_disp:
                    print(u)
        elif opt == 7:
            print('Tchau!')
            break

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nInterrompido pelo usuario')
        sys.exit(0)