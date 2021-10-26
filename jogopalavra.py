secreto = 'palmeiras'
digitadas = []
chances = 4

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if letra in digitadas:
        print(f'Você já digitou a letra {letra}!')
        continue

    if len(letra) > 1:
        print('Não vale trapacear, ein? Digite apenas uma letra: ')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Que legal! a letra {letra} existe na palavra secreta.')
    else:
        print(f'Que pena! a letra {letra} não existe na palavra secreta')
        digitadas.pop()

    secretotemporario = ''
    for letrasecreta in secreto:
        if letrasecreta in digitadas:
            secretotemporario += letrasecreta
        else:
            secretotemporario += '*'

    if secretotemporario == secreto:
        print(f'Você ganhou! A palavra secreta é {secretotemporario}!')
        break
    else:
        print(f'A palavra secreta está assim {secretotemporario}')

    if letra not in secreto:
        chances -= 1
        print(f'você tem {chances}!')
        print()
