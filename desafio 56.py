
total = 0
idmaior = 0
idmenor = 0
mulheres = 0
soma = 0

for pessoa in range(1, 5):
    print('--- {}º PESSOA ---' .format(pessoa))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO (F/M): ')).upper()

    if pessoa == 1:
        idmaior = idade

    else:
        if pessoa > 1 and idade > idmaior:
            idmaior = idade
            if pessoa > 1 and idade == idmaior and sexo == 'M':
             nmaior = nome

        if pessoa > 1 and idade < 20 and sexo == 'F':
            mulheres += 1 + 1

    total += idade
    media = total / pessoa

print('a média das idades do grupo é de {} anos'.format(media))
print('a maior idade do grupo é {} anos e pertence a {}' .format(idmaior, nmaior))
print('a quantidade de mulheres com menos de 20 anos é de {}' .format(mulheres))
