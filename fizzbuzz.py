def num(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return f'fizzbuzz, {n1} é divisível por 3 e 5'
    if n1 % 3 == 0:
        return f'fizz, {n1} é divisível por 3'
    if n1 % 5 == 0:
        return f'buzz, {n1} é divisível por 5'
    else:
        return n1

from random import randint

for i in range(100):
   aleatorio = randint(0, 100)
   print(num(aleatorio))


