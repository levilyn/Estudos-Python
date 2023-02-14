from random import randint

print('*' * 20)
print('GAME: PAR OU IMPAR')
print('*' * 20)
print('JOGADOR x COMPUTADOR')
print('*' * 20)

v = 0

while True:
    jogador = int(input('digite um número de 0 a 10: '))
    escolha = str(input('Par ou Ímpar? ')).lower().strip()[0]
    comp = randint(0, 10)
    total = jogador + comp
    res = 'p' or 'i'
    print('*' * 20)

    if int(total % 2) == 0:
        print(f'você jogou o número {jogador} e o computador jogou o número {comp}, ou seja, a soma deu {total} → PAR')
        res = 'p'

    if int(total % 2) == 1:
        print(f'você jogou o número {jogador} e o computador jogou o número {comp}, ou seja, a soma deu {total} → IMPAR')
        res = 'i'

    if escolha == res:
        print('Você venceu!\nvamos de novo!')
        v += 1
        print('*' * 20)

    if escolha != res:
        print('*' * 20)
        print(f'VOCÊ PERDEU!\nVocê venceu {v} vezes!')
        break
