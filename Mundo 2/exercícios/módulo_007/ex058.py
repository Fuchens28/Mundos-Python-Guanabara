# Melhore o jogo DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram nescessários para vencer

import random

num = random.randint(0, 10)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

n = -1 
tentativas = 0

while n != num:
    n = int(input('Qual número foi escolhido entre 0 e 10? '))
    tentativas += 1
    print('Analisando número...')
    if n < num:
        print('Mais... Tente novamente.')
    elif n > num:
        print('Menos... Tente novamente.')

print(f'Parabéns! Você acertou o número {num} com {tentativas} tentativa(s)!')
