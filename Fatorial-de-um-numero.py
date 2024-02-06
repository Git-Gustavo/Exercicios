# Fatorial de um número
'''
Crie um programa que recebe um número e ímprime o fatorial
 daquele número
 # Método 5Q's para montar um algorítimo:

 Analise criticamente o problema e descubra:
 (Tente explicar este problema para você mesmo em voz alta e
 peça mais informações/investigue mais até voce entender
 completamente o problema.)

 1. Quais são os dados de entrade necessários?
 -> Numero


 2. O que devo fazer com estes dados?
 -> Eu devo calcular o fatorial do número que for passado para o 
 meu programa e o exibir na tela


 3. Quais são as restrições deste problema?
 -> Deve ser um valor positivo
 -> Deve ser um numero inteiro

 4. Qual é o resultado esperado?
 -> O resultado esperado neste caso é que o fatorial
 do numero providenciado seja exibido


 5. Qual é a sequencia de passos a ser feita para o
 resultado esperado?
 -> input numero
 if numero > 0
 if numero = inteiro
 fatorial = 1
 loop de 1 a numero
    fatorial = fatorial * numero
print(fatorial)
'''
numero = int(input('Digite um número'))
if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item
print(fatorial)
