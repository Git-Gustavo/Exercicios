# Projeto - Chute o número
'''
Escreva um programa que, ao iniciar gera um valor aleatorio 1 a 10 e permite que o
 usuario chute um numero ate que o valor aleatorio gerado seja chutado corretamente

O programa deve informar se o chute foi acima ou abaixo ou igual ao valor aleatorio
 gerado no inicio do programa.

 #Método 5Q's para montar o algorítimo:

 Analise criticamente o problema e descubra:
 (Tente explicar este problema para voce mesmo em voz alta até voce compreender
 completamente o problema.)

 1. Quais são os dados de entrade necessários?
 -> valor aleatório de 1 a 10
 -> chute do usuário

 2. O que devo fazer com estes dados?
 -> Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no início
 do programa e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no
início do programa

 3. Quais são as restrições deste problema?
 -> O numero que deve ser chutado e gerado pode ser apenas entre 1 a 10

 4. Qual é o resultado esperado?
 -> O resultado esperado é que o programa deve informar se o chute foi acima ou abaixo ou igual ao valor aleatorio
 gerado no inicio do programa.

 5. Qual é a sequencia de passos a ser feita para o
 resultado esperado?
 --------
 input valor_aleatorio de 1 a 10
 input chute
 if chute > valor_aleatorio
    print "Chute foi maior que o valor gerado"
if chute < valor_aleatorio
    print "Chute foi menor que o valor gerado"
if chute = valor_aleatorio
'''
import random

valor_aleatorio = random.randint(1, 10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10  '))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!')
