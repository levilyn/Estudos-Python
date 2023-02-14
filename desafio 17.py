import math

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
h = math.hypot(ca, co)
print('a hipotenusa vai medir {:.2f}' .format(h))
