'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua trceira vez chegando atrasado, 
então pode sim, caso contrario ira tomar uma suspenção
'''
numero_de_atrasos = 0
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, porém caso tome mais 1 faltas, irá ser suspenso')
else:
    print('Pode entrar')
