def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)
