
print(' \033[0;32m EMPRÉSTIMO BANCÁRIO')

casa = float(input('Qual o valor da casa? '))
salário = float(input('Qual o seu salário? '))
anos = int(input('em quantos anos irá pagar? '))
meses = anos * 12
pagamento = casa / meses

print('ANALISANDO PEDIDO...')
if pagamento > salário * 0.3:
    print('\033[0;31m SEU EMPRÉSTIMO FOI NEGADO!')

else:
    print('EMPRÉSTIMO EFETUADO!')
