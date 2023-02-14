viagem = float(input('digite a distância de sua viagem e descubra o total que será gasto na passagem: '))

if viagem <= 200:
    preco = viagem * 0.50
    print('o total que irá gastar de passagem será o valor de R${}' .format(preco))

else:
    preco2 = viagem * 0.45
    print('o total que irá gastar de passagem será o valor de R${}' .format(preco2))
