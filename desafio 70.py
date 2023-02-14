print('-*' * 20)
print('             LYN´S STORE')
print('-*' * 20)

prod = menor = f = total = 0

while True:
    produto = str(input('NOME DO PRODUTO: ')).upper()
    preco = float(input('VALOR DO PRODUTO: R$'))
    opc = str(input('QUER ADICIONAR MAIS PRODUTOS (S/N)? ')).lower().strip()[0]
    total += preco
    prod += 1

    if prod == 1 or preco < menor:
        menor = preco
        f = produto

    if preco >= 1000:
        prod += 1

    if opc == 'n':
        break

print('-*' * 20)
print(f'O VALOR TOTAL DE SUA COMPRA É DE R${total}\nVOCÊ COMPROU {prod} PRODUTOS ACIMA DE R$1000\nO PRODUTO MAIS BARATO'
      f' DE SUA COMPRA FOI {f}')
print(f'Obrigada pela preferência! Volte sempre!')
