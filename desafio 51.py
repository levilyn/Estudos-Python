print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA (P.A)')

termo = int(input('termo: ')) #primeiro termo
razao = int(input('razão: '))  #quantos num irá pular
soma = termo + (10 - 1) * razao  #quantidade de termo

for pa in range(termo, razao + soma, razao):
    print(pa, end=', ')
print('...')
