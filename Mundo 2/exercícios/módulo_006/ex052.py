# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
# Só e divisivel por 1 e por ele mesmo 

n = int(input('Digite um número para ver se ele é primo: '))
eh_primo = True

if n <= 1:
    eh_primo = False
else:
    for c in range(2, n):
        if n % c == 0:
            eh_primo = False
            break

if eh_primo:
    print(f'O número {n} é primo')
else: 
    print(f'O número {n} não é primo')

