resposta = input("Você recebeu uma promoção E OU esta sol? 'Sim sim ou sim ou não' ").split()
res = resposta[0]
res2 = resposta[1]
if res == 'não' and res2 == 'não':
    print('Me deixa só quero chorar')
elif res == 'sim' and res2 == 'sim':
    print('Vamos tomar um soverte e Quero uma tv pro Jogo')
elif res == 'sim' or res2 == 'sim':

