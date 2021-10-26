from random import randint
CPF = str(randint(100000000, 999999999))

if not CPF.isnumeric():
    print('por favor, digite apenas números!')
else:
    lista = CPF
    lista_a = list(lista)
    inicio1 = 11
    inicio2 = 12
    valor1 = 0
    valor2 = 0

    for num in range(9):
        inicio1 -= 1
        valor1 += int((lista_a[num])) * inicio1

    num1 = 11 - (valor1 % 11)
    if num1 > 9:
        num1 = 0
        lista_a += str(num1)

    elif num1 <= 9:
        num1 = num1
        lista_a += str(num1)

    for num in range(10):
        inicio2 -= 1
        valor2 += int((lista_a[num])) * inicio2

    num2 = 11 - (valor2 % 11)
    if num2 > 9:
        num2 = 0
        lista_a += str(num2)

    elif num2 <= 9:
        num2 = num2
        lista_a += str(num2)
lista_a = ''.join(lista_a)
print(lista_a)