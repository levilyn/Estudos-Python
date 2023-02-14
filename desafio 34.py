a = float(input('digite seu salário e descubra o valor de seu aumento: '))

if a <= 1250:
    aumento = (15/100) * a + a
    print('antes o seu salário era de R${}, porém com o aumento de 15%, ele ficou com o total de R${}'
          .format(a, aumento))
if a > 1250:
    aumento = (10/100) * a + a
    print('antes o seu salário era de R${}, porém com o aumento de 10%, ele ficou com o total de R${}'
          .format(a, aumento))
