name = str(input('Digite seu nome completo: ')).strip()

name_upper = name.upper()
name_lower = name.lower()
name_len = len(name) - name.count(' ')
name_splited = name.split()
first_name = name_splited[0]
first_name_len = len(first_name)

print("""Analisando seu nome...
        Seu nome em maiúsculas é {}
        Seu nome em minúsculas é {}
        Seu nome ao todo tem {} letras
        Seu primeiro nome é {} e ele tem {} letras
    """.format(name_upper, name_lower, name_len, first_name, first_name_len))
