from math import trunc

number = float(input('Digite um numero: '))

print('O valor digitado foi {} e sua porção inteira é {}'.format(
    number, trunc(number)))

print('O valor digitado foi {} e sua porção inteira é {}'.format(
    number, int(number)))
