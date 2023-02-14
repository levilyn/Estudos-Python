import datetime
print('DETECTOR DE MAIORIDADE')

atual = datetime.date.today().year
idmaior = 0
idmenor = 0

for a in range(0, 7):
    ano = int(input('DIGITE UM ANO DE NASCIMENTO: '))
    idade = atual - ano

    if idade < 18:
        idmenor += 1
    else:
         idmaior += 1

print('temos {} pessoas maiores de idade' .format(idmaior))
print('temos {} pessoas menores de idade' .format(idmenor))
