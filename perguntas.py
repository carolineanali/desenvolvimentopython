
print('Esse pequeno programa irá testar seus conhecimentos gerais! escolha entre as alternativas [a, b, c ou d] a seguir e boa sorte! ')
print()
perguntas = {
    'Primeira pergunta': {
        'pergunta': 'Qual o número mínimo de jogadores numa partida de futebol?',
        'respostas': {'a': 8, 'b': 10, 'c': 11, 'd': 7},
        'resposta_correta': 'd',
    },
    'Segunda pergunta': {
        'pergunta': 'Qual personagem folclórico costuma ser agradado pelos caçadores com a oferta de fumo?',
        'respostas': {'a': 'Saci', 'b': 'Caipora', 'c': 'Mula sem cabeça', 'd': 'Lobisomen'},
        'resposta_correta': 'b',
    },
    'Terceira pergunta': {
        'pergunta': 'Quanto é 35 * 8?',
        'respostas': {'a': 280, 'b': 269, 'c': 275, 'd': 290},
        'resposta_correta': 'a',
    },
}

respostas_corretas = 0
respostas_possiveis = ['a', 'b', 'c', 'd']

for chave, valor in perguntas.items():
    print(f"{chave}: {valor['pergunta']}")

    print('Escolha uma resposta:')
    for rk, rv in valor['respostas'].items():
        print(f'{rk}: {rv}')

    sua_resposta = input('Digite sua resposta: ')

    if sua_resposta in respostas_possiveis:
        if sua_resposta == valor['resposta_correta']:
            print('Resposta correta! Você é um gênio!')
            respostas_corretas += 1
        else:
            print('Você errou!')

    else:
        print('Digite uma das alternativas solicitadas! ')
        continue

    print()

qtd_perguntas = len(perguntas)
acertos = respostas_corretas / qtd_perguntas * 100
if acertos == 100:
    print('Você arrasou! Acertou todas as respostas. Parabéns!')
elif acertos == 70:
    print(f'Você passou por média. Das {qtd_perguntas} perguntas do questionário {acertos:.2f}% estavam corretas ')
elif acertos < 70:
    print(f'Reprovou! Você acertou apenas {acertos:.2f}. Tente Novamente')