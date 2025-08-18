# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

num = random.randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

nume = int(input('Qual o número que foi escolido entre 0 e 5? '))

print('Analisando o número...')

if num == nume: 
    print('Parabéns, você acertou o número')

else:
    print('Que pena, não foi dessa vez')