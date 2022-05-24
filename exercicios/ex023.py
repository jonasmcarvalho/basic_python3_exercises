number = int(input('Digite um numero inteiro de 4 digitos: '))

unity = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print('Analisando o numero {}'.format(number))
print('Unidade: {}'.format(unity))
print('Dezena: {}'.format(ten))
print('Centena: {}'.format(hundred))
print('Milhar: {}'.format(thousand))
