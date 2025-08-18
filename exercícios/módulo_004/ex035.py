# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triãngulo 

r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Suas retas formam um triângulo')
    
else: 
    print('Suas retas não formam um triângulo')

