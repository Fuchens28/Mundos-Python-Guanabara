# Crie um programa que simule o funcionamento de um caixa eletrõnico. No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas
# de R$50, R$20, R10 e R$1.


cedulas = [50, 20, 10, 1]

print('-=' * 10)
print('BANCO SAFU')
print('-=' * 10)


while True:
    valor = int(input('Qual valor você quer sacar? R$'))

    if valor <= 0:
        print('Valor inválido. Tente novamente.')
        continue 

    total = valor 
    for ced in cedulas:  
        if total >= ced:
            n_cedulas = total // ced
            total -= n_cedulas * ced
            print(f'Total de {n_cedulas} cédulas de R${ced}')

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('Volte sempre ao nosso banco! Tenha um bom dia!')
