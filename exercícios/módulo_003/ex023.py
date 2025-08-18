# Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados
# ex: digite um número: 1834 -> unidade:4; dezena:3; centena:8; milhar:1

num = int(input('Digite um número de 0 a 9999: '))

num_str = str(num).zfill(4)
divide = list(num_str)

print(f'Unidade:[3] \nDezena:[2] \nCentena:[1] \n Milhar[0]')

