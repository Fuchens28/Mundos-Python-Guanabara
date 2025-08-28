# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual é o valor do seu salário mensal? R$ '))
tempo = int(input('Em quantos anos deseja pagar? '))

parcela = valor / (tempo * 12)  # total de meses

print(f'\nPara pagar uma casa de R${valor:.2f} em {tempo} anos, a prestação será de R${parcela:.2f}.')

if parcela <= salario * 0.3:
    print('Empréstimo aprovado!')
else:
    print(' Infelizmente, o empréstimo não foi aprovado. A parcela excede 30% do seu salário.')
