salary = float(input('Digite o salario: '))

print('O salario {} com 15"%" de almento é {:.2f}: '.format(
    salary, salary + salary * 15 / 100))
