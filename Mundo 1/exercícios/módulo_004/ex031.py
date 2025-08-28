# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 
# por km para viagens de até 200km e R$0,45 para viagens mais longas.

dist = int(input('Qual a distância em Km da sua viagem? '))

if dist <= 200:
    p1 = dist * 0.50
    print(f'O valor da sua passagem é de {p1}')

else:
    p2 = dist * 0.45
    print(f'O valor da sua passagem é de {p2}')