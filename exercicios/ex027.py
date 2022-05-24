name = str(input('Digite seu nome completo: ')).strip()

name_splited = name.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(name_splited[0]))
print('Seu último nome é {}'.format(name_splited[len(name_splited) - 1]))
