from random import randint
from time import sleep

computer = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

player = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(3)

if player == computer:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}!'.format(computer, player))
