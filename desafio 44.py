
print('\033[1;32m GERENCIADOR DE PAGAMENTOS \033[0m')

prod = float(input('Olá, seja bem vindo! Qual o valor TOTAL da compra? R$'))
pag = float(input('formas de pagamento disponiveis:\n'
                  '(1) à vista em dinheiro/cheque\n'
                  '(2) à vista no cartão\n'
                  '(3) até 2x no cartão\n'
                  '(4) 3x ou mais no cartão\n'
                  'INFORME A FORMA DE PAGAMENTO ESCOLHIDA: '))
if pag == 1:
    desc = prod * 10/100
    valor = prod - desc
    print('você escolheu paga à vista/cheque e ganhou 10% de desconto!'
          ' o valor final é de R${}' .format(valor))

elif pag == 2:
    desc = prod * 5/100
    valor = prod - desc
    print('você escolheu pagar à vista no cartão e ganhou 5% de desconto!'
          'o valor final é de R${}' .format(valor))

if pag == 3:
    parc = int(input('em quantas parcelas? '))
    if parc == 1:
        print('você escolheu pagar parcela única de R${}' .format(prod))
    if parc == 2:
        valor = prod / 2
    print('você escolheu parcelar 2x no cartão, então irá pagar o valor de R${} por mês' .format(valor))

if pag == 4:
    parc = int(input('em quantas parcelas? '))
    aum = prod * 20/100
    v = prod + aum
    mes = v / parc
    print('você escolheu parcelar {}x no cartão, com isso houve um aumento de 20% de juros'
          ' então sua compra ficou com o total de R${}, pagando parcelas de {} por mês' .format(parc, v, mes))
else:
    print('\033[1;31m COMPRA INVÁLIDA, TENTE NOVAMENTE!')
