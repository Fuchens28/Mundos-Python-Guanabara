# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint 
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Escolha sua jogada: '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 11)
print(f'O computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if jogador < 0 or jogador > 2:
    print('Jogada Inválida')
elif computador == jogador:
    print('EMPATE')
elif (jogador == 0 and computador == 2) or \
     (jogador == 1 and computador == 0) or \
     (jogador == 2 and computador == 1):
    print('JOGADOR VENCE')
else:
    print('COMPUTADOR VENCE')




