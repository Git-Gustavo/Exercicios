nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('A quantidade de letras em seu nome é: {}'.format(len(nome) - nome.count(' ')))
print('Letras 1° nome: {}'.format(len(nome)))
#print('Seu nome tem {} letras no primeiro nome '.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))
print(separa)