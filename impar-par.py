'''
4 dividido por 2 é igual a 2, sem resto. Portanto, 4 % 2 retorna 0.

Já 5 dividido por 2 é igual a 2, com resto 1. Portanto, 5 % 2 retorna 1. 5/2--> 2° da taboada ->4 
mas o 5 não faz divisão por inteiro e sobra o "1", aqui só se aplica numeros inteiros 
'''

Numero = int(input('Digite um numero e desvendarei se é par ou impar'))
if Numero % 2 == 0:
    print('Numero é par')
else:
    print('Numero é impar')
