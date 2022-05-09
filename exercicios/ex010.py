money = int(input('Digite um valor em dinheiro: '))

dolarValue = 5.0087

print('Com o valor de {:.2f} reais, você consegue comprar {:.2f} dolares atualmente.'.format(
    money, money / dolarValue))
