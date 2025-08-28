# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Considere US$1,00 = R$3,27
# Faça com o atual também

d = float(input('Dígite o valor em Reais que você tem: '))
print(f'O valor convertido para US$: {d/3.27}')
print(f'O valor convertido para US$ atual: {d/5.40}')