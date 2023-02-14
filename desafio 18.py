import math

a = float(input('digite um ângulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('o seno de {} é {:.2f}\no cosseno de {} é {:.2f}\na tangente de {} é {:.2f}' .format(a, s, a, c, a, t))
