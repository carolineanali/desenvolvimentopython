
hora = input('Digite um horário entre 0 e 23: ')

if hora.isnumeric():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Digite um horário entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite!')

else:
    print('Digite um valor numérico')
