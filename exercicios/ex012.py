value = int(input('Digite o valor do produro: '))

print('O valor do produto com 5"%" de desconto é: {:.2f}'.format(
    value - value * 5 / 100))
