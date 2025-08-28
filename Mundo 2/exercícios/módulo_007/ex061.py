# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrrando os 10 primeiros termos da progressão usando a estrutura while

print('Gerador de PA')
print('-=' * 10)

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da sua PA: '))

termo = n1
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end = '')
    termo += r
    cont += 1

print('ACABOU')
