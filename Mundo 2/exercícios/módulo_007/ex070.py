# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A - Qual é o total gasto na compra;
# B - Quantos produtos custam mais de R$1000;
# C - Qual é o nome do produto mais barato.

total = cont = mais_mil = 0
menor_preco = 0
nome_barato = ''

print('-=' * 5)
print('LOJA SAFU')
print('-=' * 5)

while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))

    total += preco
    cont += 1 

    if preco > 1000:
        mais_mil += 1

    # Definir o mais barato
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        nome_barato = nome 

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break 

print(f'\nO total da compra foi R${total:.2f}')
print(f'Temos {mais_mil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi "{nome_barato}" que custou R${menor_preco:.2f}')
