import random

print('vamos jogar? vou pensar em um número de 0 a 5 e você vai tentar adivinhar')
p = int(input('digite um número de 0 a 5: '))
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n1, n2, n3, n4, n5]
r = random.choice(lista)

print('meu número escolhido foi {}' .format(r))
if p == r:
    print('parabéns, você acertou!')
else:
    print('errou! a sorte não estava com você desta vez...')

#GUANABARA RESPOSTA

from random import randint
from time import sleep
computador = randint(0, 5)
print('vou pensar em um número de 0 a 5, tente adivinhar')
jogador = int(input('em que número pensei? '))
print('processando...')
sleep(3)

if jogador == computador:
    print('parabens você conseguiu!')
else:
    print('ganhei! você perdeu!')
