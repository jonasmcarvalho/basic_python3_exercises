distance = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {}Km'.format(distance))

price = distance * 0.50 if distance <= 200 else distance * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(price))
