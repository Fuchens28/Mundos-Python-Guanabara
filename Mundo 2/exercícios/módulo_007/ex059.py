# Crie um programa que leia dois valores e mostre um menu na tela: 
# [1] somar
# [2] multiplicar
# [3] maior 
# [4] novos números 
# [5] sair do programa 
# Seu programa deverá realizar a operação solicitada em cada caso

n1 = float(input('Escolha seu 1° número: '))
n2 = float(input('Escolha o seu 2° valor: '))

op = ''

while op != '5':
    print(f'''Escolha uma opção
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] novos números
    [ 5 ] Sair do programa''')

    op = int(input('Sua opção é: '))

    if op == 1:
        print(f'A soma dos números {n1} e {n2} é igual a {n1 + n2}')
    
    elif op == 2:
        print(f'A multiplicação dos números {n1} e {n2} é igual a {n1 * n2}')

    elif op == 3:
        maior = max(n1, n2)
        print(f'O maior número entre {n1} e {n2} é {maior}')

    elif op == 4:
        n1 = float(input('Escolha seu 1° número: '))
        n2 = float(input('Escolha o seu 2° valor: '))

    elif op == 5:
        print('Encerrando programa...')
        break 

    else:
        print('Opção invalida. Tente novamente...')
