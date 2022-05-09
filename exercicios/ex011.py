height = int(input('Qual é a altura da parede: '))
width = int(input('Qual é a largura da parede: '))

area = height * width

print('A area é {}.'.format(area))
print('Para pintar uma area de {}, é necessario {} litros de tinta.'.format(area, area / 2))
