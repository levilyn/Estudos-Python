import random
from time import sleep

#configuração da escolha do computador

opc = ('pedra', 'papel', 'tesoura')
comp = random.randint(0, 2)
esc = opc[comp]

#configuração da escolha do jogador

print('suas opções de jogo:\n'
      '(0) PEDRA\n'
      '(1) PAPEL\n'
      '(2) TESOURA')
jogador = int(input('sua escolha: '))

print('\033[1;34mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!\033[0m')


#jogo

print('o computador escolheu {}' .format(esc))
print('você escolheu {}' .format(opc[jogador]))

if comp == 0: #PEDRA
      if jogador == 0:
            print('EMPATE')
      elif jogador == 1:
            print('VOCÊ VENCEU')
      elif jogador == 2:
            print('COMPUTADOR VENCEU')

if comp == 1: #PAPEL
      if jogador == 0:
            print('COMPUTADOR VENCEU')
      elif jogador == 1:
            print('EMPATE')
      elif jogador == 2:
            print('VOCÊ VENCEU')

if comp == 2: #TESOURA
      if jogador == 0:
            print('VOCÊ VENCEU')
      elif jogador == 1:
            print('COMPUTADOR VENCEU')
      elif jogador == 2:
            print('EMPATE')
