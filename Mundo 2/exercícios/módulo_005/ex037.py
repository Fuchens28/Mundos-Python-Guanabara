# Escreva um programa que leia um número inteiro qualquer a peça para o usuário escolher a base de conversão
# -> 1 - para binário; -> 2 - para octal; -> 3 para hexadecimal

num = int(input('Escolha um número: '))

opcao = int(input('''Escolha uma base de conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
Sua opção: '''))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')

elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')

elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')

else:
    print('Opção inválida. Tente novamente.')

