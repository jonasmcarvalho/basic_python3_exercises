altura = int(input('Qual é a altura da parede: '))
largura = int(input('Qual é a largura da parede: '))

area = altura * largura

print('A area é {}.'.format(area))
print('Para pintar uma area de {}, é necessario {} litros de tinta.'.format(area, area / 2))
