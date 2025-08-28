# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# -> À vista dinheiro/cheque: 10% de desconto
# -> À vista no cartão: 5% de desconto
# -> Em até 2x no cartão: preço normal
# -> 3x ou mais no cartão: 20% de juros

preco = float(input('Qual o valor do produto? '))

fp = int(input('''Escolha a forma de pagamento:
[1] À vista no Dinheiro/Cheque
[2] À vista no cartão
[3] Parcelado em até 2x no cartão
[4] Parcelado em 3x ou mais no cartão
Digite: '''))

if fp == 1:
    print(f'Você ganhou 10% de desconto e o valor de sua compra é de R${preco - (preco * 0.1)}')

elif fp == 2:
    print(f'Você ganhou 5% de desconto, e o valor de sua compra é de R${preco - (preco * 0.05)}')

elif fp == 3: 
    print(f'Você não ganhou desconto e o valor de sua compra é de R${preco}')

else:
    print(f'Sua compra teve um juros de 20% e o valor da sua compra é R${preco + (preco * 0.2)}')

