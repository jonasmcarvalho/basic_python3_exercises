city = (str(input('Em que cidade você nasceu: '))).strip()

city_prefix = city[:5].lower()

city_test = city_prefix == 'santo'

print(city_test)
