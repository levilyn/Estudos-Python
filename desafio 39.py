from datetime import datetime
print('ALISTAMENTO MILITAR')

nasc = int(input('DIGITE O ANO DE SEU NASCIMENTO: '))
alist = datetime.today().year - nasc
atual = datetime.today().year

if alist < 18:
    tempo = 18 - alist
    print('você ainda não está no periodo de alistamento, ainda falta {} anos' .format(tempo))

elif alist == 18:
    print('você está na idade correta para se alistar!')

elif alist > 18:
    tempo = alist - 18
    print('você deveria ter se alistado há {} ano' .format(tempo))
    ano = atual - tempo
    print('você deveria ter se alistado no ano de {}' .format(ano))
