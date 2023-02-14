from random import randint

print('JOGADOR x COMPUTADOR')
computador = randint(0, 10)
jog = 1

while computador != 0:
    jogador = int(input('olá jogador, de 0 a 10, em que número pensei? '))
    if jogador > computador:
        print('menos... tente novamente')
        jog += 1
    if jogador < computador:
        print('mais... tente novamente')
        jog += 1
    if jogador == computador:
        print('parabéns, você venceu')
        print('para você vencer foram necessárias {} tentativas'.format(jog))
        break
