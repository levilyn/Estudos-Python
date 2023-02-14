
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'os números sorteados foram {numeros}')
print(f'o maior valor sorteado foi {max(numeros)}')
print(f'o menor valor sorteado foi {min(numeros)}')
