# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão


n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da sua PA: '))

for c in range(n1, n1 + (10 * r), r):
    print(f'{c}', end=' -> ')

print('ACABOU')














