from datetime import datetime

print('DESCUBRA SUA CATEGORIA')
ano = int(input('digite o ANO de seu nascimento: '))
idade = datetime.today().year - ano

if idade <= 9:
    print('você está na categoria MIRIM')

elif idade <= 14:
    print('você está na categoria INFANTIL')

elif idade <= 19:
    print('você está na categoria JÚNIOR')

elif idade <= 25:
    print('Você está na categoria SÊNIOR')

elif idade > 25:
    print('Você está na categoria MASTER')
