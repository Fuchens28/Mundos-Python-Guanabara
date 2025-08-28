# Faça um programa que leia três números e mostre qual é o maior e qual é o menor 

n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha outro número: '))
n3 = float(input('Escolha o terceiro número: '))

maximo = max(n1,n2,n3)
menor = min(n1,n2,n3)

print(f'O seu maior número é {maximo} e o seu menor número é {menor}')

