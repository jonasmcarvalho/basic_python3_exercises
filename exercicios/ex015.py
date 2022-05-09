km_traveled = float(input('Digite a quilometragem percorrida: '))
rented_days = float(input('Digite a quantidade de dias alugado: '))

daily_value = rented_days * 60
km_traveled_value = km_traveled * 0.15

total_payable = daily_value + km_traveled_value

print('O veiculo ficou {:.0f} dias alugado, rodou {:.2f} quilometros, e o total a pagar é {:.2f}'.format(
    rented_days, km_traveled, total_payable))
